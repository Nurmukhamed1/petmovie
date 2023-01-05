from rest_framework import serializers
from movies.models import Movies
from cadres.models import MovieShots


class MovieDetailSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    movieshots = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = [
            "title",
            "tagline",
            "description",
            "poster",
            "movieshots",
            "year",
            "country",
            "directors",
            "actors",
            "genres",
            "world_premiere",
            "budget",
            "fees_in_usa",
            "fees_in_world",
        ]

    @staticmethod
    def get_directors(data):
        return data.directors.values('name')

    @staticmethod
    def get_actors(data):
        return data.actors.values('name')

    @staticmethod
    def get_genres(data):
        return data.genres.values("name")

    def get_movieshots(self, data):  # TODO: make it normal
        request = self.context.get("request")
        q = MovieShots.objects.filter(movie=data.pk)
        response = []
        for i in range(len(q)):
            response.append(request.build_absolute_uri(q[i].image.url))
        return response
