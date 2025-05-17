from django.contrib import admin
from .models import Movie, Series

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'imdb', 'source_id')
    list_filter = ('genres',)
    search_fields = ('title', 'genres__name')

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'imdb', 'source_id')
    list_filter = ('genres',)
    search_fields = ('title', 'genres__name')