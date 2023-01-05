from rest_framework import mixins, viewsets

from reviews.models import Reviews
from reviews.api.v1.serializers import ReviewSerializer


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
