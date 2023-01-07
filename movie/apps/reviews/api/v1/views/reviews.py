from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets

from reviews.api.v1.serializers.reviews import ReviewReplySerializer
from reviews.models import Reviews
from reviews.api.v1.serializers import ReviewSerializer
from utils.mixins import ActionSerializerMixin


@extend_schema(tags=["reviews"])
class ReviewViewSet(
    ActionSerializerMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reviews.objects.all()
    serializer_class = ReviewReplySerializer
    serializer_classes = {
        "list": ReviewReplySerializer,
        "create": ReviewSerializer,
    }

    def get_queryset(self):
        if self.action == "list":
            return Reviews.objects.filter(parent=None)
        return self.queryset

    def perform_create(self, serializer):
        parent_id = self.request.data["parent"]
        parent_name = self.queryset.get(pk=parent_id).name
        serializer.save(text=parent_name + ", " + self.request.data["text"])
