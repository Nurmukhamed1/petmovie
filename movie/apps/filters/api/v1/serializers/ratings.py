from rest_framework import serializers

from ratings.models import Ratings


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = (
            "id",
            "star",
        )
