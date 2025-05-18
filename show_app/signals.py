from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie, Series

@receiver([post_save, post_delete], sender=Movie)
def clear_movie_cache(sender, **kwargs):
    cache.delete_pattern("movie_list*")
    cache.delete_pattern("movie_detail*")

@receiver([post_save, post_delete], sender=Series)
def clear_series_cache(sender, **kwargs):
    cache.delete_pattern("series_list*")
    cache.delete_pattern("series_detail*")
