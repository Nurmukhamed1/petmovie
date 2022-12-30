from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
