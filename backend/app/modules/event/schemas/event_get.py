from pydantic import BaseModel

class EventGet(BaseModel):
    """
    Docstring for EventGet
    Схема для фильтров запроса ИВЕНТОВ
    """
    id: int

    