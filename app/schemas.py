from pydantic import BaseModel
from .enums import Role

class UserCreate(BaseModel):
    name: str
    email: str
    role: Role = Role.developer

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None