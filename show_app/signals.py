from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Movie, Series


@receiver(post_save, sender=Movie)
@receiver(post_delete, sender=Movie)
def clear_movie_cache(sender, instance, **kwargs):
    cache.delete_pattern("movie_list*")
    cache.delete_pattern(f"movie_detail*/{instance.source_id}*")


@receiver(post_save, sender=Series)
@receiver(post_delete, sender=Series)
def clear_series_cache(sender, instance, **kwargs):
    cache.delete_pattern("series_list*")
    cache.delete_pattern(f"series_detail*/{instance.source_id}*")
