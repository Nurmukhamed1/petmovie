from rest_framework import serializers
from movies.models import Movies


class MovieDetailSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = [
            "title",
            "tagline",
            "description",
            "poster",
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
