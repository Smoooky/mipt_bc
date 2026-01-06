from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints

Password = Annotated[
    str,
    StringConstraints(min_length=2, max_length=32)
]

class RegisterUserPayload(BaseModel):
    email: EmailStr
    password: Password
    full_name: str