from rest_framework import serializers
from .models import Movie, Series, Genre, Person

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = PersonSerializer(many=True)
    producers = PersonSerializer(many=True)
    actors = PersonSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            'source_id', 'title', 'release_year',
            'genres', 'directors', 'producers', 'actors',
            'lover', 'imdb', 'story'
        ]

class SeriesSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    directors = PersonSerializer(many=True)
    producers = PersonSerializer(many=True)
    actors = PersonSerializer(many=True)

    class Meta:
        model = Series
        fields = [
            'source_id', 'title', 'release_year',
            'genres', 'directors', 'producers', 'actors',
            'lover', 'imdb', 'story', 'seasons'
        ]