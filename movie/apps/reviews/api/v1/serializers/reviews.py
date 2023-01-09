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

    def create(self, validated_data):
        parent = self.validated_data["parent"]
        if parent:
            parent_name = Reviews.objects.get(pk=parent.id).name
            validated_data["text"] = parent_name + ", " + validated_data["text"]
        return super().create(validated_data)


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
