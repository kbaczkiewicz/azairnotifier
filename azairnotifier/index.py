import uvicorn
from fastapi import FastAPI
from azairnotifier.config.di.container import Container
from azairnotifier.infrastructure.api.http import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=["azairnotifier.infrastructure.api.http.endpoints"])
    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)

    return app


app = create_app()
if __name__ == '__main__':
    uvicorn.run("index:app", host='0.0.0.0', port=80, reload=True)
