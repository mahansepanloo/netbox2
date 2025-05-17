from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']), 
        ]

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),  
        ]

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True, blank=True)
    source_id = models.CharField(max_length=255, unique=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    directors = models.ManyToManyField(Person, related_name='movies_directed')
    producers = models.ManyToManyField(Person, related_name='movies_produced')
    actors = models.ManyToManyField(Person, related_name='movies_acted')
    lover = models.IntegerField(null=True, blank=True)
    imdb = models.FloatField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-release_year']
        indexes = [
            models.Index(fields=['source_id']),
            models.Index(fields=['release_year']),
        ]

class Series(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True, blank=True)
    source_id = models.CharField(max_length=255, unique=True)
    genres = models.ManyToManyField(Genre, related_name='series')
    directors = models.ManyToManyField(Person, related_name='series_directed')
    producers = models.ManyToManyField(Person, related_name='series_produced')
    actors = models.ManyToManyField(Person, related_name='series_acted')
    lover = models.IntegerField(null=True, blank=True)
    imdb = models.FloatField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-release_year']
        indexes = [
            models.Index(fields=['source_id']),
            models.Index(fields=['release_year']),
        ]
        
