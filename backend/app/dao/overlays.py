from app.dao.base import BaseDAO
from app.models.overlays import Overlay


class OverlaysDAO(BaseDAO):
    model = Overlay