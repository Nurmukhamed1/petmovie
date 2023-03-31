from django.urls import path, include

from rest_framework.routers import DefaultRouter

from actors.api.v1.views.actors_producers import ActorsDirectorsViewSet

router = DefaultRouter()

router.register("", ActorsDirectorsViewSet, basename="actors_directors")

urlpatterns = [
    path("", include(router.urls))
]
