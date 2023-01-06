from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets

from reviews.models import Reviews
from reviews.api.v1.serializers import ReviewSerializer


@extend_schema(tags=["reviews"])
class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        parent_id = self.request.data["parent"]
        parent_name = self.queryset.get(pk=parent_id).name
        serializer.save(text=parent_name + ", " + self.request.data["text"])
