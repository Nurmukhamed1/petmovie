from django.contrib import admin
from django.utils.safestring import mark_safe

from cadres.models import MovieShots
from reviews.models import Reviews
from .models import Movies


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class CadresInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Image"


@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [CadresInline, ReviewInline]
    readonly_fields = ("get_image",)
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image",))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="110" height="100"')

    get_image.short_description = "Poster"

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "One value was changed"
        else:
            message_bit = f"{row_update} values was changed"
        self.message_user(request, message_bit)

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 value was changed"
        else:
            message_bit = f"{row_update} values was changed"
        self.message_user(request, message_bit)

    publish.short_description = "Publish"
    publish.allowed_permissions = ("change",)

    unpublish.short_description = "Unpublish"
    unpublish.allowed_permissions = ("change",)
