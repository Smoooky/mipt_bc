from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import EventCreate, EventResponse, SpeakerResponse, SpeakerCreate, EventGet
from .service import EventService
from app.core.database import get_session

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}

@router.post(
    "",
    response_model=EventResponse,
    status_code=201
)
async def create_event(
    payload: EventCreate,
    session: AsyncSession = Depends(get_session)
):
    service = EventService(session)
    return await service.create_event(payload)
    
@router.post(
    "/speaker",
    response_model=SpeakerResponse,
    status_code=201
)
async def create_speaker(
    payload: SpeakerCreate,
    session: AsyncSession = Depends(get_session)
):
    service = EventService(session)
    return await service.create_speaker(payload)
    
@router.get(
    "/",
    response_model=EventResponse
)
async def get_event(
    id: int,
    session: AsyncSession = Depends(get_session),
):
    service = EventService(session)
    return await service.get_event(id)
    