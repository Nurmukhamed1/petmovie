from django.contrib import admin
from .models import Genres


@admin.register(Genres)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
