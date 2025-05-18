Movie and Series Content Management System
Project Overview
This project is a content management system (CMS) designed to store and display information about movies and series. It consists of two main components:

Django Backend: A REST API built with Django REST Framework to manage and serve movie and series data.
Scrapy Scraper: A web scraper to collect movie and series data from the Namava website (namava.ir) and store it in a PostgreSQL database.

The system uses PostgreSQL as the database to store information about movies, series, genres, and persons (directors and actors).

Project Architecture
The project is modular and consists of the following components:
1. Django Backend

Models (models.py):
Genre: Stores genre information.
Person: Stores information about individuals (directors and actors).
BaseContent: An abstract base model for movies and series.
Movie and Series: Specific models for movies and series.


Views (views.py):
MovieViewSet and SeriesViewSet: REST API views for listing, searching, and ordering movies and series.
Caching (15 minutes) is implemented to improve performance.


Tests (test.py):
Unit tests to ensure API functionality, including tests for listing, searching, and ordering.


URLs:
API endpoints for movies (/api/movies/) and series (/api/series/).
Swagger and ReDoc documentation for the API.



2. Scrapy Scraper

Spiders:
NamavaMediaSpider: Scrapes movie data.
NamavaSerialSpider: Scrapes series data.


Pipeline (pipeline.py):
Saves scraped data to the database using Django models.
Automatically manages genres, directors, and actors.



3. Database

PostgreSQL: Used for relational data storage.
Indexes are applied on release_year for improved query performance.


Prerequisites

Python 3.8+
PostgreSQL 12+
Redis (for caching)
Scrapy
Django and Django REST Framework


Setup Instructions
1. Install Dependencies
pip install -r requirements.txt

2. Configure the Database

Create a PostgreSQL database:

createdb movie_series_db


Update the database settings in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_series_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

3. Run Migrations
python manage.py makemigrations
python manage.py migrate

4. Set Up Redis

Install and start Redis:

sudo apt-get install redis-server
systemctl start redis

5. Run the Scraper

To scrape movie data:

scrapy crawl namava_media_spider


To scrape series data:

scrapy crawl namava_serial_spider

6. Start the Django Server
python manage.py runserver

7. Access the API

List Movies: GET /api/movies/
Search Movies: GET /api/movies/?search=Inception
Order by IMDb: GET /api/movies/?ordering=-imdb
List Series: GET /api/series/
API Documentation: http://localhost:8000/swagger/


Running Tests
To execute unit tests:
python manage.py test

Tests cover:

Listing movies and series.
Searching content by title.
Ordering by IMDb and release year.


API Documentation
API documentation is available via Swagger and ReDoc:

Swagger: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/


Key Features

Caching: API responses are cached for 15 minutes to enhance performance.
Scraper: Prevents duplicate data processing using processed_ids.
Database: Indexes are used to optimize query performance.


Future Enhancements

Add authentication to the API.
Support advanced filtering (e.g., by genre).
Enhance the scraper to collect additional data (e.g., posters).

