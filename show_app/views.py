from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Movie, Series
from .serializers import MovieSerializer, SeriesSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.prefetch_related("genres", "directors", "actors").all()
    serializer_class = MovieSerializer
    lookup_field = "source_id"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "genres__name"]
    ordering_fields = ["release_year", "imdb"]


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.prefetch_related("genres", "directors", "actors").all()
    serializer_class = SeriesSerializer
    lookup_field = "source_id"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "genres__name"]
    ordering_fields = ["release_year", "imdb"]
