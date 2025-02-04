from datetime import datetime
from typing import Optional, List

import uuid
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    avatar_url: Optional[str] = None
    riot_id: Optional[str] = None
    hdev_api_key: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    avatar_url: Optional[str] = None
    riot_id: Optional[str] = None
    hdev_api_key: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OverlayResponse(BaseModel):
    id: uuid.UUID
    background_color: str
    text_color: str
    primary_color: str
    progressbar_color: str

    class Config:
        from_attributes = True


class UserWithOverlays(UserResponse):
    overlays: List[OverlayResponse] = list
