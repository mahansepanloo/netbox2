from rest_framework import serializers
from .models import Movie, Series, Genre, Person


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "id"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name", "id"]


class BaseContentSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    directors = PersonSerializer(many=True, read_only=True)
    actors = PersonSerializer(many=True, read_only=True)

    class Meta:
        fields = [
            "source_id",
            "title",
            "release_year",
            "genres",
            "directors",
            "actors",
            "lover",
            "imdb",
            "story",
        ]

class MovieSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta):
        model = Movie

class SeriesSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta):
        model = Series
