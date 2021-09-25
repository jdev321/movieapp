from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()

@app.get("/settings")
async def settings(settings: Settings = Depends(get_settings)):
    return {
        "environment": settings.environment,
        "testing": settings.testing
    }