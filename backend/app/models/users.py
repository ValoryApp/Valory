from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)

    twitch_id = Column(String, nullable=True)
    twitch_display_name = Column(String, nullable=True)

    riot_id = Column(String, nullable=True)
    hdev_api_key = Column(String, nullable=True)

    overlays = relationship("Overlay", back_populates="user")
