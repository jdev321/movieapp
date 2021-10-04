import logging

from fastapi import FastAPI

from app.api import settings, movies
from app.db import init_db

from app.utils.http import client_start, client_end

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(settings.router)
    application.include_router(movies.router, prefix="/movie", tags=["movie"])

    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    await client_start()
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
    await client_end()