from django.db import models


class Actors(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and producers"
        verbose_name_plural = "Actors and producers"
