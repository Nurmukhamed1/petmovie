from rest_framework import serializers
from movies.models import Movies
from actors.models import Actors


class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = [
            "title",
            "tagline",
            "poster",
            "directors",
            "actors",
            "genres",
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

