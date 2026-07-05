from fastapi import FastAPI
from contextlib import asynccontextmanager
from app import models, routes
from app.database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Users API", version="1.0.0", lifespan=lifespan)

    

    app.include_router(routes.router)
    return app


app = create_app()
