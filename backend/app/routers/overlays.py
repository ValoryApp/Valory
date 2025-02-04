import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.models.overlays import Overlay
from app.schemas.overlays import OverlayCreate, OverlayResponse, OverlayUpdate

router = APIRouter()


@router.post("/", response_model=OverlayCreate)
async def create_overlay(overlay: OverlayCreate, session: AsyncSession = Depends(get_session)) -> Overlay:
    overlay = Overlay(**overlay.model_dump())
    session.add(overlay)
    await session.commit()
    await session.refresh(overlay)
    return overlay


@router.get('/', response_model=list[Overlay])
async def get_overlays(session: AsyncSession = Depends(get_session)) -> list[Overlay]:
    result = await session.exec(select(Overlay))
    overlays = result.all()
    return [overlay for overlay in overlays]


@router.get("/{overlay_id}", response_model=OverlayResponse)
async def get_overlay(overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> OverlayResponse:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.exec(statement)
    overlay = result.first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")
    return overlay


@router.patch("/{overlay_id}", response_model=OverlayResponse)
async def update_overlay(
        overlay_id: uuid.UUID,
        overlay_update: OverlayUpdate,
        session: AsyncSession = Depends(get_session)
) -> OverlayResponse:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.exec(statement)
    overlay = result.first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")

    for key, value in overlay_update.model_dump(exclude_unset=True).items():
        setattr(overlay, key, value)

    await session.commit()
    await session.refresh(overlay)

    return overlay


@router.delete("/{overlay_id}")
async def delete_overlay(overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.exec(statement)
    overlay = result.first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")

    await session.delete(overlay)
    await session.commit()
    return {"message": "Overlay deleted"}
