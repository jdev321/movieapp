from tortoise import fields, models

class Movie(models.Model):
    adult = fields.BooleanField()
    movie_id = fields.IntField()
    original_title = fields.TextField()
    popularity = fields.FloatField()
    video = fields.BooleanField()

    def __str__(self) -> str:
        return self.original_title