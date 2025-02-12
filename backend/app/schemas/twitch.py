
from pydantic import BaseModel


class STwitchOauth(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None
    expires_in: int | None = None
    token_type: str | None = None


class STwitchOauthCreate(STwitchOauth):
    pass


class STwitchOauthResponse(STwitchOauth):
    user_id: int

    class Config:
        from_attributes = True
