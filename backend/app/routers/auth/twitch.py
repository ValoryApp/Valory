import random
import string
from typing import Optional
from urllib.parse import urlencode

import aiohttp
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_session
from app.models.overlays import Overlay
from app.models.twitch_oauth import TwitchOauth
from app.models.users import User

router = APIRouter()


async def generate_random_string(length: int) -> str:
    """
    Generates a random alphanumeric string of the given length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


async def make_request(method: str, url: str, headers: Optional[dict] = None, data: Optional[dict] = None) -> dict:
    """
    Sends an asynchronous HTTP request.
    """
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, data=data) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail=f"Failed request to {url}")
            return await response.json()


async def fetch_user_info(access_token: str) -> Optional[dict]:
    """
    Fetches Twitch user information using the provided access token.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": settings.TWITCH_CLIENT_ID
    }
    data = await make_request("GET", "https://api.twitch.tv/helix/users", headers=headers)
    return data.get("data", [{}])[0] if data.get("data") else None


async def fetch_twitch_token(data: dict) -> dict:
    """
    Fetches an OAuth2 token from the Twitch API.
    """
    return await make_request("POST", "https://id.twitch.tv/oauth2/token", data=data)


@router.get("/login", summary="Initiate Twitch OAuth login")
async def twitch_login() -> RedirectResponse:
    """
    Redirects the user to the Twitch authorization page with a generated state parameter.
    """
    state = await generate_random_string(16)
    query_params = {
        "response_type": "code",
        "client_id": settings.TWITCH_CLIENT_ID,
        "redirect_uri": settings.REDIRECT_URI,
        "state": state
    }
    response = RedirectResponse(url=f"https://id.twitch.tv/oauth2/authorize?{urlencode(query_params)}")
    response.set_cookie("twitch_state", state)
    return response


@router.get("/callback", summary="Handle Twitch OAuth callback")
async def callback(request: Request, session: AsyncSession = Depends(get_session)) -> RedirectResponse:
    """
    Handles the Twitch OAuth callback, exchanges code for tokens, fetches user info, and stores it.
    """
    code, state = request.query_params.get("code"), request.query_params.get("state")
    if not code or state != request.cookies.get("twitch_state"):
        raise HTTPException(status_code=400, detail="Invalid or missing state")

    token_data = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": settings.REDIRECT_URI,
    }
    api_response = await fetch_twitch_token(token_data)
    user_info = await fetch_user_info(api_response.get("access_token"))

    if user_info:
        statement = select(User).where(User.twitch_id == user_info['id'])
        result = await session.execute(statement)
        user_db = result.scalars().first()

        if not user_db:
            new_user = User(
                username=user_info['login'],
                avatar_url=user_info['profile_image_url'],
                twitch_id=user_info['id'],
                twitch_display_name=user_info['display_name']
            )
            new_oauth = TwitchOauth(
                user_id=new_user.id,
                access_token=api_response.get("access_token"),
                refresh_token=api_response.get("refresh_token"),
                expires_in=int(api_response.get("expires_in")),
                token_type=api_response.get("token_type")
            )
            overlay = Overlay(user_id=new_user.id)
            session.add_all([new_user, new_oauth, overlay])
            await session.commit()

    response = RedirectResponse(
        url=f"{settings.FRONTEND_URL}/callback?access_token={api_response.get('access_token')}&expires_in={api_response.get('expires_in')}")
    response.delete_cookie("twitch_state")
    return response


@router.post("/refresh", summary="Refresh Twitch OAuth token")
async def refresh_token(refresh_token: str) -> dict:
    """
    Refreshes an expired Twitch OAuth2 access token using a refresh token.
    """
    token_data = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    return await fetch_twitch_token(token_data)
