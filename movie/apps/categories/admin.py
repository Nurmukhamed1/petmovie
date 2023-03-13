from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
