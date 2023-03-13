from django.contrib import admin
from .models import Ratings


@admin.register(Ratings)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "star", "ip")
