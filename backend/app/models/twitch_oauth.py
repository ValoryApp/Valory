from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class TwitchOauth(Base):
    __tablename__ = "twitch_oauth"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token = Column(Text, nullable=True)
    refresh_token = Column(Text, nullable=True)
    expires_in = Column(Integer, nullable=True)
    token_type = Column(String, nullable=True)

    user = relationship("User", back_populates="twitch_oauth")
