from typing import Optional

from pydantic import BaseModel

from app.schemas.overlays import SOverlayResponse
from app.schemas.twitch import STwitchOauthResponse


class SUser(BaseModel):
    username: str
    avatar_url: Optional[str] = None
    twitch_id: Optional[str] = None
    twitch_display_name: Optional[str] = None
    riot_id: Optional[str] = None
    hdev_api_key: Optional[str] = None


class SUserCreate(SUser):
    pass


class SUserResponse(SUser):
    id: int
    overlays: list[SOverlayResponse] = []
    twitch_oauth: Optional[STwitchOauthResponse] = None

    class Config:
        from_attributes = True
