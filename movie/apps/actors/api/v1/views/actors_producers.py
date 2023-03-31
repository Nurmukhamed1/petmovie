from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from actors.api.v1.serializers.actors import ActorSerializer
from actors.models.actors import Actors


@extend_schema(tags=["actors and directors"])
class ActorsDirectorsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
