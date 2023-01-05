from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies.api.v1.views import MoviesViewSet
from movies.api.v1.views.movie_details import MovieDetailViewSet

router = DefaultRouter()

router.register("", MoviesViewSet, basename="movie_list")
router.register("details", MovieDetailViewSet, basename="movie_details")

urlpatterns = [
    path("", include(router.urls)),
]
