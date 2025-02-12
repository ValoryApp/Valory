
from pydantic import BaseModel

from app.schemas.overlays import SOverlayResponse
from app.schemas.twitch import STwitchOauthResponse


class SUser(BaseModel):
    username: str
    avatar_url: str | None = None
    twitch_id: str | None = None
    twitch_display_name: str | None = None
    riot_id: str | None = None
    hdev_api_key: str | None = None


class SUserCreate(SUser):
    pass


class SUserResponse(SUser):
    id: int
    overlays: list[SOverlayResponse] = []
    twitch_oauth: STwitchOauthResponse | None = None

    class Config:
        from_attributes = True
