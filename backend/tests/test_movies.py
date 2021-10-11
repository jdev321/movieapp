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
        assert response.json()["title"] == "The Matrix"