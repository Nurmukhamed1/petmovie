from rest_framework import serializers

from reviews.models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            "email",
            "name",
            "text",
            "movie",
        ]
