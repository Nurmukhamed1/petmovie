from django_filters import rest_framework as filters


class MovieFilterSet(filters.FilterSet):
    year = filters.NumberFilter()
    country = filters.BaseInFilter()
    directors = filters.BaseInFilter()
    actors = filters.BaseInFilter()
    genres = filters.BaseInFilter()
    world_premiere = filters.DateFromToRangeFilter()
    category = filters.NumberFilter()
