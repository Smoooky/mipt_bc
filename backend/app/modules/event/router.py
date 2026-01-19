from fastapi import APIRouter, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import EventCreate, EventResponse, SpeakerResponse, SpeakerCreate, EventSearchParams, SpeakerSearchParams, PaginationSettings, EventUpdate, SpeakerUpdate, AuthRoles
from .service import EventService
from app.core.database.session import get_session
from app.core.dependencies import role_required_factory
from typing import List
from functools import partial

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

# Events

@router.post(
    "",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_event(
    payload: EventCreate,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    return await service.create_event(payload)
    
@router.patch(
    "/{id}",
    response_model=EventResponse,
    status_code=status.HTTP_200_OK
)
async def update_event(
    id: int,
    payload: EventUpdate,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    return await service.update_event(id, payload)

@router.get(
    "/{id}",
    response_model=EventResponse,
    status_code=status.HTTP_200_OK
)
async def get_event(
    id: int,
    session: AsyncSession = Depends(get_session),
):
    service = EventService(session)
    return await service.get_event(id)

@router.get(
    "/search",
    response_model=List[EventResponse],
    status_code=status.HTTP_200_OK
)
async def search_event(
    params: EventSearchParams = Depends(),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    session: AsyncSession = Depends(get_session)
):
    service = EventService(session)
    settings = PaginationSettings(limit=limit, offset=offset)
    return await service.search_events(params, settings)

@router.delete(
    '/{id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_event(
    id: int,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    await service.delete_event(id)
    return

# Speakers

@router.post(
    "/speaker",
    response_model=SpeakerResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_speaker(
    payload: SpeakerCreate,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    return await service.create_speaker(payload)

@router.patch(
    '/speaker/{id}',
    response_model=SpeakerResponse,
    status_code=status.HTTP_200_OK
)
async def update_speaker(
    id: int,
    payload: SpeakerUpdate,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    return await service.update_speaker(id, payload)
    
@router.get(
    '/speaker/search',
    response_model=List[SpeakerResponse],
    status_code=status.HTTP_200_OK
)
async def search_speaker(
    params: SpeakerSearchParams = Depends(),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    session: AsyncSession = Depends(get_session)
):
    service = EventService(session)
    settings = PaginationSettings(limit=limit, offset=offset)
    return await service.search_speakers(params, settings)

@router.get(
    '/speaker/{id}',
    response_model=SpeakerResponse,
    status_code=status.HTTP_200_OK
)
async def get_speaker(
    id: int = Path(..., description="ID спикера"),
    session: AsyncSession = Depends(get_session)
):
    service = EventService(session)
    return await service.get_speaker(id)

@router.delete(
    '/speaker/{id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_speaker(
    id: int,
    session: AsyncSession = Depends(get_session),
    user_data = Depends(role_required_factory(AuthRoles.ADMIN, AuthRoles.MANAGER))
):
    service = EventService(session)
    await service.delete_speaker(id)
    return