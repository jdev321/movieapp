from tortoise import fields, models

class Movie(models.Model):
    movie_id = fields.IntField(pk=True)
    adult = fields.BooleanField()
    id = fields.IntField()
    original_title = fields.TextField()
    popularity = fields.FloatField()
    video = fields.BooleanField()

    def __str__(self) -> str:
        return self.original_title