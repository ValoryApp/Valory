from typing import Optional

from pydantic import BaseModel

from app.schemas.overlays import OverlayResponse
from app.schemas.twitch import TwitchOauthResponse


class UserBase(BaseModel):
    username: str
    avatar_url: Optional[str] = None
    twitch_id: Optional[str] = None
    twitch_display_name: Optional[str] = None
    riot_id: Optional[str] = None
    hdev_api_key: Optional[str] = None


class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    overlays: list[OverlayResponse] = []
    twitch_oauth: Optional[TwitchOauthResponse] = None

    class Config:
        from_attributes = True
