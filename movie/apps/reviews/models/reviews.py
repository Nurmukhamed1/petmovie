from django.db import models

from movies.models import Movies


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=128)
    text = models.TextField()
    parent = models.ForeignKey(
        to="self", on_delete=models.SET_NULL, blank=True, null=True, related_name="reply"
    )
    movie = models.ForeignKey(to=Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - {self.name}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
