from django.test import TestCase
from rest_framework.test import APIClient
from show_app.models import Movie, Series

class MovieViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Inception",
            source_id="123",
            imdb=8.8,
            release_year=2010
        )
        Movie.objects.create(
            title="Interstellar",
            source_id="456",
            imdb=8.6,
            release_year=2014
        )

    def test_movie_list_success(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_movie_retrieve_success(self):
        response = self.client.get(f"/api/movies/{self.movie.source_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.movie.title)

    def test_movie_search_by_title(self):
        response = self.client.get("/api/movies/?search=Inception")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertIn("Inception", response.data["results"][0]["title"])

    def test_movie_ordering_by_imdb(self):
        response = self.client.get("/api/movies/?ordering=-imdb")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 2)
        self.assertGreaterEqual(
            response.data["results"][0]["imdb"], response.data["results"][1]["imdb"]
        )


class SeriesViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.series = Series.objects.create(
            title="Breaking Bad",
            source_id="789",
            imdb=9.5,
            release_year=2008
        )
        Series.objects.create(
            title="Better Call Saul",
            source_id="101",
            imdb=8.9,
            release_year=2015
        )

    def test_series_list_success(self):
        response = self.client.get("/api/series/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_series_retrieve_success(self):
        response = self.client.get(f"/api/series/{self.series.source_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.series.title)

    def test_series_search_by_title(self):
        response = self.client.get("/api/series/?search=Breaking")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertIn("Breaking", response.data["results"][0]["title"])

    def test_series_ordering_by_release_year(self):
        response = self.client.get("/api/series/?ordering=-release_year")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 2)
        self.assertGreaterEqual(
            response.data["results"][0]["release_year"], response.data["results"][1]["release_year"]
        )
