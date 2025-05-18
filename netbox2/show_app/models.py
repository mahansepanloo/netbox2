from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class BaseContent(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True, blank=True)
    source_id = models.CharField(max_length=255, unique=True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Person, related_name="%(class)s_directed")
    actors = models.ManyToManyField(Person, related_name="%(class)s_acted")
    lover = models.IntegerField(null=True, blank=True)
    imdb = models.FloatField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-release_year"]
        indexes = [models.Index(fields=["release_year"])]


class Movie(BaseContent):
    pass


class Series(BaseContent):
    pass
