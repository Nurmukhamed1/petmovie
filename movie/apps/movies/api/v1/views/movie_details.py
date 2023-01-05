from rest_framework import mixins, viewsets

from movies.api.v1.serializers.movie_details import MovieDetailSerializer
from movies.models import Movies


class MovieDetailViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Movies.objects.all()
    serializer_class = MovieDetailSerializer
