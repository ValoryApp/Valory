from typing import Optional

from pydantic import BaseModel


class TwitchOauthBase(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None
    token_type: Optional[str] = None

class TwitchOauthCreate(TwitchOauthBase):
    pass

class TwitchOauthResponse(TwitchOauthBase):
    user_id: int

    class Config:
        from_attributes = True