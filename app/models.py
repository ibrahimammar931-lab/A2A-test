from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .enums import Role

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String, default=Role.developer)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="Pending")

    assigned_user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")