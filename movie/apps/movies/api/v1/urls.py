from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies.api.v1.views import MoviesViewSet

router = DefaultRouter()

router.register("", MoviesViewSet, basename="movie_list")

urlpatterns = [
    path("", include(router.urls)),
]
