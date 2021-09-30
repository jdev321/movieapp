from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()

@router.get("/settings")
async def settings(settings: Settings = Depends(get_settings)):
    return {
        "environment": settings.environment,
        "testing": settings.testing
    }