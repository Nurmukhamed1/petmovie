from rest_framework import serializers

from reviews.models import Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = (
            "id",
            "parent",
            "movie",
            "email",
            "name",
            "text",
        )


class ReviewReplySerializer(serializers.ModelSerializer):
    children = ReviewSerializer(source="reply", many=True)

    class Meta:
        model = Reviews
        fields = (
            "id",
            "email",
            "name",
            "text",
            "children"
        )
