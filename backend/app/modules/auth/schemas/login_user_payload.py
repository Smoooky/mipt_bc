from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated

Password = Annotated[
    str,
    StringConstraints(min_length=8, max_length=64)
]

class LoginUserPayload(BaseModel):
    email: EmailStr
    password: Password