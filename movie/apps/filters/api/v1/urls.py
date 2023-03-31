from django.urls import path, include

from rest_framework.routers import DefaultRouter

from filters.api.v1.views.actors_directors import ActorsDirectorsViewSet
from filters.api.v1.views.genres import GenresViewSet
from filters.api.v1.views.ratings import RatingsViewSet

router = DefaultRouter()

router.register("actors", ActorsDirectorsViewSet, basename="actors_directors")
router.register("genres", GenresViewSet, basename="genres")
router.register("ratings", RatingsViewSet, basename="ratings")

urlpatterns = [
    path("", include(router.urls))
]
