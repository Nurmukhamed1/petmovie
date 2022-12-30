from django.db import models

from actors.models import Actors
from categories.models import Categories
from genre.models import Genres


class Movies(models.Model):
    title = models.CharField(max_length=128)
    tagline = models.CharField(max_length=128)
    description = models.TextField()
    poster = models.ImageField()
    year = models.IntegerField()
    country = models.CharField(max_length=128)
    directors = models.ManyToManyField(to=Actors, related_name="film_director")
    actors = models.ManyToManyField(to=Actors, related_name="film_actor")
    genres = models.ManyToManyField(to=Genres)
    world_premiere = models.DateField()
    budget = models.IntegerField()
    fees_in_usa = models.IntegerField()
    fees_in_world = models.IntegerField()
    category = models.ForeignKey(to=Categories, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
