from rest_framework import mixins, viewsets
from rest_framework.generics import RetrieveAPIView
from movies.api.v1.serializers.movie_details import MovieDetailSerializer
from movies.models import Movies


class MovieDetailViewSet(RetrieveAPIView):
    lookup_field = "pk"
    queryset = Movies.objects.all()
    serializer_class = MovieDetailSerializer
