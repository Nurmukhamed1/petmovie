from django.db import models

from movies.models import Movies

class MovieShots(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to="movie_shots/")
    movie = models.ForeignKey(to=Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Screen shot of a movie"
        verbose_name_plural = "Screen shots of a movie"
