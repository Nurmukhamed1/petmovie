from drf_spectacular.utils import extend_schema
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
        queryset = super(ReviewViewSet, self).get_queryset()
        if self.action == "list":
            queryset = queryset.filter(parent=None)
        return queryset
