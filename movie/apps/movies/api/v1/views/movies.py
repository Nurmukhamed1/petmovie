from rest_framework import mixins, viewsets
from movies.models import Movies
from movies.api.v1.serializers import MovieSerializer


class MoviesViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()
