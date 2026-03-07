from fastapi import FastAPI

from app import models, routes
from app.database import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Users API", version="1.0.0")

    @app.on_event("startup")
    def on_startup() -> None:
        Base.metadata.create_all(bind=engine)

    app.include_router(routes.router)
    return app


app = create_app()
