from rest_framework import serializers

from cadres.models import MovieShots


class MovieShotSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source="image")

    class Meta:
        model = MovieShots
        fields = (
            "title",
            "image",
        )
