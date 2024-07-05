import uvicorn
from fastapi import FastAPI
from azairnotifier.config.di.container import Container
from azairnotifier.infrastructure.api.http import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=["azairnotifier.infrastructure.api.http.endpoints"])
    _app = FastAPI()
    _app.container = container
    _app.include_router(endpoints.router)

    return _app


app = create_app()

