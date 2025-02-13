import random
import string
from urllib.parse import urlencode

import aiohttp
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_session
from app.utils.auth import authenticate_user, create_access_token

router = APIRouter()


async def generate_random_string(length: int) -> str:
    """
    Generates a random alphanumeric string of the given length.
    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


async def make_request(
    method: str, url: str, headers: dict | None = None, data: dict | None = None
) -> dict:
    """
    Sends an asynchronous HTTP request.
    """
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, data=data) as response:
            if response.status != 200:
                raise HTTPException(
                    status_code=response.status, detail=f"Failed request to {url}"
                )
            return await response.json()


async def fetch_user_info(access_token: str) -> dict | None:
    """
    Fetches Twitch user information using the provided access token.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": settings.TWITCH_CLIENT_ID,
    }
    data = await make_request(
        "GET", "https://api.twitch.tv/helix/users", headers=headers
    )
    return data.get("data", [{}])[0] if data.get("data") else None


async def fetch_twitch_token(code: str) -> dict:
    """
    Fetches an OAuth2 token from the Twitch API.
    """
    token_data = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": settings.REDIRECT_URI,
    }

    return await make_request("POST", "https://id.twitch.tv/oauth2/token", data=token_data)


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
        "state": state,
    }
    response = RedirectResponse(
        url=f"https://id.twitch.tv/oauth2/authorize?{urlencode(query_params)}"
    )
    response.set_cookie("twitch_state", state)
    return response


@router.get("/callback", summary="Handle Twitch OAuth callback", response_model=None)
async def callback(request: Request, session: AsyncSession = Depends(get_session)) -> HTTPException | RedirectResponse:
    """
    Handles the Twitch OAuth callback, exchanges code for tokens, fetches user info, and stores it.
    """
    code, state = request.query_params.get("code"), request.query_params.get("state")
    if not code or state != request.cookies.get("twitch_state"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    api_response = await fetch_twitch_token(code)
    user_info = await fetch_user_info(api_response.get("access_token"))

    user = await authenticate_user(session, user_info)

    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    access_token = await create_access_token({"sub": user.id})

    response = RedirectResponse(url=settings.APP_FRONTEND_URL + "/callback")
    response.set_cookie(
        "Authorization",
        value=f"Bearer {access_token}",
        max_age=1800,
        expires=1800,
        samesite="lax",
        secure=not settings.DEBUG,
    )
    response.delete_cookie("twitch_state")
    return response
