from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Actors


@admin.register(Actors)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Image"
