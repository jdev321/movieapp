from app.models.pydantic import MoviePayloadSchema
from app.models.tortoise import Movie

from app.utils import http

import os
import random
from dotenv import load_dotenv
from datetime import datetime

from typing import Union

load_dotenv()

key = os.environ.get("API_KEY")

random.seed(datetime.now())



async def get():
    randomNumber = random.randint(1, 500000)

    movie_id = await Movie.filter(movie_id=randomNumber).first().values()

    BASE_URL = "https://api.themoviedb.org/3/movie/{random}?api_key={key}&langauge=en-US".format(key=key, random=movie_id[0]["id"])

    async with http.CLIENT_SESSION.get(BASE_URL) as response:
        text = await response.json()

    movie_info = {
        "title": text["original_title"],
        "tagline": text["tagline"],
        "description": text["overview"],
        "release": text["release_date"],
        "poster": text["poster_path"]
    }

    return movie_info
        
    

    

    
  
