from pydantic import BaseModel

class MoviePayloadSchema(BaseModel):
    id: int

class MovieResponseSchema(BaseModel):
    title: str
    tagline: str
    description: str
    release: str
    poster: str = None