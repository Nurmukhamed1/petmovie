from rest_framework import serializers

from actors.models import Actors


class ActorsDirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = (
            "id",
            "name",
        )
