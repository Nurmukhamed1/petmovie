from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from movies.models import Movies
from movies.api.v1.serializers import MovieSerializer


@extend_schema(tags=["movies"])
class MoviesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = MovieSerializer
    queryset = Movies.objects.filter(draft=False)
