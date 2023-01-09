from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from movies.api.v1.serializers.movies import MovieDetailSerializer
from movies.models import Movies
from movies.api.v1.serializers import MovieSerializer
from utils.mixins import ActionSerializerMixin


@extend_schema(tags=["movies"])
class MoviesViewSet(
    ActionSerializerMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()
    serializer_classes = {
        "list": MovieSerializer,
        "retrieve": MovieDetailSerializer,
    }

    def get_queryset(self):
        queryset = super(MoviesViewSet, self).get_queryset()
        if self.action == "list":
            queryset = queryset.filter(draft=False)
        return queryset
