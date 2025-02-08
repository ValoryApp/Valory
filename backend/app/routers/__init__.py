from fastapi import APIRouter

from app.routers import overlays
from app.routers.auth import twitch

api_router = APIRouter()
api_router.include_router(overlays.router, prefix="/overlay", tags=["Overlay"])
api_router.include_router(twitch.router, prefix="/auth/twitch", tags=["Auth & Tokens"])
