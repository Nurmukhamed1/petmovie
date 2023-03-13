from django.contrib import admin
from .models import Actors


@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
