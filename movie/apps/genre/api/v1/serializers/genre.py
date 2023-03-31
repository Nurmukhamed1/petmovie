from rest_framework import serializers

from genre.models import Genres


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = (
            "id",
            "name",
        )
