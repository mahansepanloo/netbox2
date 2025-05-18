from rest_framework import viewsets
from django.views.decorators.cache import cache_page
from .models import Movie, Series
from .serializers import MovieSerializer, SeriesSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.decorators import method_decorator


class BaseContentViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "genres__name"]
    ordering_fields = ["release_year", "imdb"]

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class MovieViewSet(BaseContentViewSet):
    queryset = Movie.objects.prefetch_related("genres", "directors", "actors")
    serializer_class = MovieSerializer
    lookup_field = "source_id"


class SeriesViewSet(BaseContentViewSet):
    queryset = Series.objects.prefetch_related("genres", "directors", "actors")
    serializer_class = SeriesSerializer
    lookup_field = "source_id"
