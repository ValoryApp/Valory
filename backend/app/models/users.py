from datetime import datetime
from typing import List

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import text


class UserBase(SQLModel):
    username: str = Field(default=None, nullable=False)
    email: str = Field(default=None, nullable=False)

    avatar_url: str = Field(default=None, nullable=True)

    riot_id: str = Field(default=None, nullable=True)
    hdev_api_key: str = Field(default=None, nullable=True)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(),
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(),
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)"),
        },
    )


class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

    overlays: List["Overlay"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    pass
