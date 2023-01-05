from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reviews.api.v1.views import ReviewViewSet

router = DefaultRouter()

router.register("", ReviewViewSet, basename="reviews")

urlpatterns = [
    path("", include(router.urls)),
]
