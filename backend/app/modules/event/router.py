from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import EventCreate, EventResponse
from .service import EventService
from ...core.database import get_session

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
    event = await service.create_event(payload)
    return event