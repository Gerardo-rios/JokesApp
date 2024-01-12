from fastapi import FastAPI

from .events.event_handler import register_routers
from .routers import version


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(version)
    register_routers(app, "api.routers.v1", "v1")
    return app
