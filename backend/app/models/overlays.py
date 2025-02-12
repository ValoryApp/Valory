import uuid

from sqlalchemy import UUID, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Overlay(Base):
    __tablename__ = "overlays"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    background_switch = Column(Boolean, default=True, nullable=False)
    progressbar_switch = Column(Boolean, default=True, nullable=False)
    statistics_switch = Column(Boolean, default=False, nullable=False)

    background_color = Column(String, default="#07090e", nullable=False)
    text_color = Column(String, default="#ffffff", nullable=False)
    primary_color = Column(String, default="#bebebf", nullable=False)
    progressbar_color = Column(String, default="#00ffe3", nullable=False)
    win_color = Column(String, default="#00ffe3", nullable=False)
    lose_color = Column(String, default="#ff7986", nullable=False)

    user = relationship("User", back_populates="overlays")
