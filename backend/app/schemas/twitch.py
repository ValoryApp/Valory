from typing import Optional

from pydantic import BaseModel


class STwitchOauth(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None
    token_type: Optional[str] = None


class STwitchOauthCreate(STwitchOauth):
    pass


class STwitchOauthResponse(STwitchOauth):
    user_id: int

    class Config:
        from_attributes = True
