import unittest
from app.models.tortoise import Movie
from unittest import mock
import pytest

@pytest.mark.asyncio
class MovieRoutesTest(unittest.TestCase):
    async def test_get_random_movie(test_app_with_db):
        movie = Movie(
            adult=False,
            id=603,
            original_title='The Matrix',
            popularity=64.09,
            video=False,
        )
        await movie.save()
        with mock.patch("app.api.crud.random.randint", lambda x, y: movie.movie_id):
            response = await test_app_with_db.get("/movie/")
        assert response == {
            "title": "The Matrix",
            "tagline": "Welcome to the Real World.",
            "description": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
            "release": "1999-03-30",
            "poster": "/lh4aGpd3U9rm9B8Oqr6CUgQLtZL.jpg"
        }