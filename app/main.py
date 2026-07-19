from fastapi import FastAPI
from .database import Base, engine
from .routes import tasks, users
from .auth import oauth2_scheme, verify_token
from .services import tasks_service, users_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {
        "message": "TaskFlow API"
    }