import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_session
from app.models.overlays import Overlay
from app.schemas.overlays import SOverlay, SOverlayCreate, SOverlayResponse

router = APIRouter()


@router.post("/", response_model=SOverlayCreate)
async def create_overlay(
    overlay: SOverlayCreate, session: AsyncSession = Depends(get_session)
) -> Overlay:
    """
    Creates a new overlay in the database.

    This endpoint allows the creation of a new overlay by providing the necessary details.

    :param overlay: The details of the overlay to create (OverlayCreate schema).
    :param session: AsyncSession dependency for database operations.
    :return: The created overlay (OverlayCreate response model).
    """
    overlay = Overlay(**overlay.dict())
    session.add(overlay)
    await session.commit()
    await session.refresh(overlay)
    return overlay


@router.get("/", response_model=list[SOverlayResponse])
async def get_overlays(session: AsyncSession = Depends(get_session)) -> list[Overlay]:
    """
    Retrieves a list of all overlays from the database.

    This endpoint returns all overlays stored in the database.

    :param session: AsyncSession dependency for database operations.
    :return: List of overlays (OverlayResponse schema).
    """
    result = await session.execute(select(Overlay))
    overlays = result.scalars().all()
    return [overlay for overlay in overlays]


@router.get("/{overlay_id}", response_model=SOverlayResponse)
async def get_overlay(
    overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> Overlay:
    """
    Retrieves a specific overlay by its ID.

    This endpoint returns the details of a single overlay, identified by the provided overlay ID.

    :param overlay_id: UUID of the overlay to retrieve.
    :param session: AsyncSession dependency for database operations.
    :return: The overlay (OverlayResponse schema).
    :raises HTTPException: If the overlay is not found.
    """
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.execute(statement)
    overlay = result.scalars().first()

    if not overlay:
        raise HTTPException(status_code=404, detail="Overlay not found")
    return overlay


@router.patch("/{overlay_id}", response_model=SOverlayResponse)
async def update_overlay(
    overlay_id: uuid.UUID,
    overlay_update: SOverlay,
    session: AsyncSession = Depends(get_session),
) -> Overlay:
    """
    Updates an existing overlay by its ID.

    This endpoint allows partial updates to an existing overlay, where only the provided fields are modified.

    :param overlay_id: UUID of the overlay to update.
    :param overlay_update: The update data (OverlayBase schema).
    :param session: AsyncSession dependency for database operations.
    :return: The updated overlay (OverlayResponse schema).
    :raises HTTPException: If the overlay is not found.
    """
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
async def delete_overlay(
    overlay_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> dict[str, bool]:
    """
    Deletes an overlay by its ID.

    This endpoint deletes the specified overlay from the database.

    :param overlay_id: UUID of the overlay to delete.
    :param session: AsyncSession dependency for database operations.
    :return: A message indicating that the overlay was deleted.
    :raises HTTPException: If the overlay is not found.
    """
    statement = select(Overlay).where(Overlay.id == overlay_id)
    result = await session.execute(statement)
    overlay = result.scalars().first()

    if not overlay:
        return {"status": False, "message": "Overlay not found"}

    await session.delete(overlay)
    await session.commit()
    return {"status": True, "message": "Overlay deleted"}
