from django.db import models


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Star"
        verbose_name_plural = "Stars"
        ordering = ["value"]
