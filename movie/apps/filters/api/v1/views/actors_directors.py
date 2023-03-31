from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from filters.api.v1.serializers.actors_directors import ActorsDirectorsSerializer
from actors.models.actors import Actors


@extend_schema(tags=["filters"])
class ActorsDirectorsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Actors.objects.all()
    serializer_class = ActorsDirectorsSerializer
