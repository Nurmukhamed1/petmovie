from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies.api.v1.views import MoviesViewSet
from movies.api.v1.views.movie_details import MovieDetailViewSet

router = DefaultRouter()

router.register("", MoviesViewSet, basename="movie_list")
# router.register("<int:pk>", MovieDetailViewSet, basename="movie_details")

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/", MovieDetailViewSet.as_view(), name="movie_details")
]
