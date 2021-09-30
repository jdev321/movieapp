from pydantic import BaseModel

class MoviePayloadSchema(BaseModel):
    id: int