import random
import string
from typing import Optional
from urllib.parse import urlencode

import aiohttp
from fastapi import APIRouter, HTTPException, Request, Depends, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_session
from app.models.overlays import Overlay
from app.models.twitch_oauth import TwitchOauth
from app.models.users import User

router = APIRouter()


def generate_random_string(length: int) -> str:
    """
    Generate a random alphanumeric string of the given length.

    :param length: Length of the generated string.
    :return: Randomly generated string.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


async def fetch_user_info(access_token: str) -> Optional[dict | HTTPException]:
    """
    Fetch the Twitch user's information using the provided access token.

    :param access_token: The OAuth2 access token for the Twitch user.
    :return: A dictionary containing user information (id, username, display_name, avatar_url),
             or raises an HTTPException if the request fails.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": settings.TWITCH_CLIENT_ID
    }

    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.twitch.tv/helix/users", headers=headers) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail="Failed to fetch user info")

            data = await response.json()

    if data and "data" in data and data["data"]:
        user = data["data"][0]

        user_data = {
            "id": user['id'],
            "username": user['login'],
            "display_name": user["display_name"],
            "avatar_url": user["profile_image_url"]
        }

        return user_data
    return


async def fetch_twitch_token(data: dict) -> dict:
    """
    Fetch an OAuth2 token from the Twitch API.

    :param data: Dictionary containing OAuth2 token request parameters.
    :return: JSON response containing the token information.
    :raises HTTPException: If the request fails.
    """
    async with aiohttp.ClientSession() as session:
        async with session.post("https://id.twitch.tv/oauth2/token", data=data) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail="Failed to fetch tokens")
            return await response.json()


@router.get("/login", summary="Initiate Twitch OAuth login")
async def twitch_login() -> RedirectResponse:
    """
    Initiates the Twitch OAuth2 login by redirecting the user to the Twitch authorization page.

    This function generates a random state string, stores it in a cookie, and redirects the user to
    the Twitch authorization URL.

    :return: RedirectResponse to the Twitch authorization page.
    """
    state = generate_random_string(16)

    query_params = {
        "response_type": "code",
        "client_id": settings.TWITCH_CLIENT_ID,
        "redirect_uri": settings.REDIRECT_URI,
        "state": state
    }
    response = RedirectResponse(url=f"https://id.twitch.tv/oauth2/authorize?{urlencode(query_params)}")

    response.set_cookie(
        key="twitch_state",
        value=state,
    )
    return response


@router.get("/callback", summary="Handle Twitch OAuth callback")
async def callback(request: Request, session: AsyncSession = Depends(get_session)) -> RedirectResponse:
    """
    Handles the Twitch OAuth2 callback and exchanges the authorization code for an access token.

    After the user grants permission to the app on Twitch, this function retrieves the authorization
    code from the query parameters and exchanges it for an access token and refresh token. The
    access token is then used to fetch the user's information, which is stored in the database.

    :param request: FastAPI Request object containing query parameters.
    :param session: AsyncSession dependency for database operations.
    :return: RedirectResponse to the frontend with the access token and additional info.
    """
    if not request.query_params:
        raise HTTPException(status_code=400, detail="No query parameters received")

    code = request.query_params.get("code")
    state = request.query_params.get("state")
    stored_state = request.cookies.get("twitch_state")

    if not code or not state or state != stored_state:
        raise HTTPException(status_code=400, detail="Invalid or missing state")

    data = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": settings.REDIRECT_URI,
    }

    api_response = await fetch_twitch_token(data)

    access_token = api_response.get("access_token")
    refresh_token = api_response.get("refresh_token")
    expires_in = int(api_response.get("expires_in"))
    token_type = api_response.get("token_type")

    user_info = await fetch_user_info(access_token)

    if user_info:
        statement = select(User).where(User.twitch_id == user_info['id'])
        result = await session.execute(statement)
        user_db = result.scalars().first()

        if not user_db:
            new_user = User(
                username=user_info['username'],
                avatar_url=user_info['avatar_url'],
                twitch_id=user_info['id'],
                twitch_display_name=user_info['display_name']
            )

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            new_oauth = TwitchOauth(
                user_id=new_user.id,
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=expires_in,
                token_type=token_type
            )

            session.add(new_oauth)
            await session.commit()
            await session.refresh(new_oauth)

            overlay = Overlay(user_id=new_user.id)
            session.add(overlay)
            await session.commit()
            await session.refresh(overlay)

    redirect_url = (
        f"{settings.FRONTEND_URL}/callback"
        f"?access_token={access_token}"
        f"&expires_in={expires_in}"
    )

    response = RedirectResponse(url=redirect_url)
    response.delete_cookie("twitch_state")

    return response


@router.post("/refresh", summary="Refresh Twitch OAuth token")
async def refresh_token(refresh_token: str) -> dict:
    """
    Refreshes an expired Twitch OAuth2 access token using a refresh token.

    This endpoint allows the client to obtain a new access token after the old one expires,
    using the refresh token obtained during the initial authentication.

    :param refresh_token: The refresh token obtained from a previous authentication.
    :return: JSON response containing the new access token.
    """
    data = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    return await fetch_twitch_token(data)
