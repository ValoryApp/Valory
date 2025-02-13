from fastapi import APIRouter

from app.routers import auth, overlays

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth & Tokens"])
api_router.include_router(overlays.router, prefix="/overlay", tags=["Overlay"])

