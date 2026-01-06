from pydantic import BaseModel
from typing import Optional

class PaginationSettings(BaseModel):
    limit: int = 10
    offset: int = 0