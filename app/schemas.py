from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None