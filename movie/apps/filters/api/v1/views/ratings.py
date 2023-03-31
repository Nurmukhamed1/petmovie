from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets

from filters.api.v1.serializers.ratings import RatingsSerializer
from ratings.models.ratings import Ratings


@extend_schema(tags=["filters"])
class RatingsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
