from django.contrib import admin
from .models import MovieShots


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie")
