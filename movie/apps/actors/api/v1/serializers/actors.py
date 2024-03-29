from rest_framework import serializers

from actors.models import Actors


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = (
            "id",
            "name",
            "age",
            "description",
            "image",
        )
