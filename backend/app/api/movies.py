from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import MovieResponseSchema

router = APIRouter()

@router.get("/", response_model=MovieResponseSchema)
async def get_movie() -> MovieResponseSchema:
    movie_info = await crud.get()

    return movie_info