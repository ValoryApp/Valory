import uuid

from pydantic import BaseModel


class SOverlay(BaseModel):
    background_switch: bool = True
    progressbar_switch: bool = True
    statistics_switch: bool = False
    background_color: str = "#07090e"
    text_color: str = "#ffffff"
    primary_color: str = "#bebebf"
    progressbar_color: str = "#00ffe3"
    win_color: str = "#00ffe3"
    lose_color: str = "#ff7986"


class SOverlayCreate(SOverlay):
    pass


class SOverlayResponse(SOverlay):
    id: uuid.UUID
    user_id: int

    class Config:
        from_attributes = True
