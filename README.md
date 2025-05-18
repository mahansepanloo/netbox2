Netbox2
Overview
Netbox2 is a Django-based RESTful API integrated with Scrapy for web scraping and PostgreSQL as the database. The project scrapes movie and series data from Namava.ir, stores it in a PostgreSQL database, and provides endpoints to query and filter the data with caching, search, and ordering functionalities.
Features

Web Scraping: Scrapes movie and series data (title, year, genres, directors, actors, IMDb rating, etc.) from Namava.ir using Scrapy.
REST API: Endpoints for listing and retrieving movies and series with filtering and ordering.
Database: PostgreSQL with models for genres, persons, movies, and series.
Caching: API responses cached for 15 minutes using Django's caching framework.
API Documentation: Swagger and ReDoc interfaces for API documentation.

Project Structure
netbox2/
├── manage.py
├── show_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── urls.py           # App-specific URLs
│   ├── views.py          # API viewsets
│   └── pipelines.py      # Scrapy pipeline
├── vod_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── namava_spider.py  # Scrapy spiders
├── netbox2/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py           # Root URLs
│   └── wsgi.py
├── requirements.txt
└── README.md

Requirements

Python 3.8+
PostgreSQL 13+
Django 4.x
Django REST Framework
Scrapy
drf-yasg (for Swagger/ReDoc)
psycopg2 (PostgreSQL adapter)

Install dependencies:
pip install -r requirements.txt

Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd netbox2

2. Configure Environment
Create a .env file in the project root:
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your-django-secret-key
DEBUG=True

3. Set Up PostgreSQL
Create a PostgreSQL database:
CREATE DATABASE netbox2;

4. Run Migrations
Apply database migrations:
python manage.py makemigrations
python manage.py migrate

5. Run the Scrapy Spiders
To scrape movie data:
scrapy crawl namava_media_spider

To scrape series data:
scrapy crawl namava_serial_spider

6. Start the Django Server
Run the development server:
python manage.py runserver

The API will be available at http://localhost:8000/api/.
7. Access API Documentation

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

API Endpoints
Movies

List Movies: GET /api/movies/
Query Parameters:
search: Filter by title or genre (e.g., ?search=action)
ordering: Order by release_year or imdb (e.g., ?ordering=-imdb)




Retrieve Movie: GET /api/movies/<source_id>/

Series

List Series: GET /api/series/
Query Parameters:
search: Filter by title or genre
ordering: Order by release_year or imdb




Retrieve Series: GET /api/series/<source_id>/

Scrapy Spiders

NamavaMediaSpider: Scrapes movie data from Namava.ir.
NamavaSerialSpider: Scrapes series data from Namava.ir.
Spiders fetch data in pages, extract details from preview APIs, and store unique entries using source_id.

Database Models

Genre: Stores unique genre names.
Person: Stores unique names of directors and actors.
BaseContent: Abstract model for shared fields (title, release_year, source_id, etc.).
Movie: Inherits from BaseContent for movie-specific data.
Series: Inherits from BaseContent for series-specific data.

Caching
API responses are cached for 15 minutes using Django's cache_page decorator.
Running Tests
To run tests (if any):
python manage.py test

Troubleshooting

Database Issues: Verify PostgreSQL is running and DATABASE_URL is correct.
Scrapy Errors: Check logs for network or JSON parsing issues.
API Errors: Use Swagger UI for endpoint details and response codes.

