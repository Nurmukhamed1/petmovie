from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from filters.api.v1.serializers.genres import GenreSerializer
from genre.models.genres import Genres


@extend_schema(tags=["filters"])
class GenresViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
