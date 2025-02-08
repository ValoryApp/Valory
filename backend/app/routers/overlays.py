import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.overlays import Overlay
from app.schemas.overlays import OverlayCreate, OverlayResponse, OverlayBase

router = APIRouter()


@router.post("/", response_model=OverlayCreate)
async def create_overlay(overlay: OverlayCreate, session: AsyncSession = Depends(get_session)) -> Overlay:
    overlay = Overlay(**overlay.dict())
    session.add(overlay)
    await session.commit()
    await session.refresh(overlay)
    return overlay


@router.get('/', response_model=list[OverlayResponse])
async def get_overlays(session: AsyncSession = Depends(get_session)) -> list[Overlay]:
    result = await session.execute(select(Overlay))
    overlays = result.scalars().all()
    return [overlay for overlay in overlays]


@router.get("/{overlay_id}", response_model=OverlayResponse)
async def get_overlay(overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> OverlayResponse:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.execute(statement)
    overlay = result.scalars().first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")
    return overlay


@router.patch("/{overlay_id}", response_model=OverlayResponse)
async def update_overlay(
        overlay_id: uuid.UUID,
        overlay_update: OverlayBase,
        session: AsyncSession = Depends(get_session)
) -> OverlayResponse:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.execute(statement)
    overlay = result.scalars().first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")

    for key, value in overlay_update.dict(exclude_unset=True).items():
        setattr(overlay, key, value)

    await session.commit()
    await session.refresh(overlay)

    return overlay


@router.delete("/{overlay_id}")
async def delete_overlay(overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.execute(statement)
    overlay = result.scalars().first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")

    await session.delete(overlay)
    await session.commit()
    return {"message": "Overlay deleted"}
