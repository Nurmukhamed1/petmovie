from rest_framework import serializers

from actors.api.v1.serializers.actors import ActorSerializer
from cadres.api.v1.serializers.movieshots import MovieShotSerializer
from cadres.models import MovieShots
from genre.api.v1.serializers.genre import GenreSerializer
from movies.models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = (
            "id",
            "title",
            "tagline",
            "poster",
            "url",
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    directors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    # movieshots = MovieShotSerializer()
    # movieshots = serializers.SerializerMethodField()
    # movieshots = serializers.URLField()

    class Meta:
        model = Movies
        fields = (
            "title",
            "tagline",
            "description",
            "poster",
            # "movieshots",
            "year",
            "country",
            "directors",
            "actors",
            "genres",
            "world_premiere",
            "budget",
            "fees_in_usa",
            "fees_in_world",
        )

    # def get_movieshots(self, data):  # TODO: make it normal
    #     request = self.context.get("request")
    #     q = MovieShots.objects.filter(movie=data.pk)
    #     response = []
    #     for i in range(len(q)):
    #         response.append(request.build_absolute_uri(q[i].image.url))
    #     return response
