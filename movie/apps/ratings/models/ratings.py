from django.db import models

from movies.models import Movies
from ratings.models.stars_rating import RatingStar


class Ratings(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(to=RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
