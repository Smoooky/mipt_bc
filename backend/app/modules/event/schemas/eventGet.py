from pydantic import BaseModel
from app.modules.event.models.event import eventStatus
from app.modules.event.schemas.speakerResponse import speakerResponse

class EventGet(BaseModel):
    """
    Docstring for EventGet
    Схема для фильтров запроса ИВЕНТОВ
    """
    id: int

    