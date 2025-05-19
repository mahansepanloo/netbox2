
---

# 🎬 Movie and Series Content Management System

---

## 🔥 Project Overview

A Content Management System (CMS) designed to store and display information about movies and series, consisting of two main components:

* **Django Backend:** A REST API built with Django REST Framework to manage and serve movie and series data.
* **Scrapy Scraper:** A web scraper to collect movie and series data from the Namava website (namava.ir) and store it in a PostgreSQL database.

---

## 🏗️ Project Architecture

```plaintext
movie_series_project/
├── backend/                # Django backend app
│   ├── models.py           # Models for genres, persons, movies, and series
│   ├── views.py            # API ViewSets
│   ├── tests.py            # Unit tests
│   ├── urls.py             # API endpoints
│   └── settings.py         # Project settings
├── vod_scraper/            # Scrapy spiders
│   ├── spiders/
│   │   ├── namava_media_spider.py
│   │   
│   └── pipeline.py         # Pipeline to save scraped data to DB
├── requirements.txt        # Dependencies
└── docker-compose.yml      # Docker config
```

---

## 🧱 Components

### 1. Django Backend

* **Models (models.py)**

  ```python
  class Genre(models.Model):
      # Stores genres

  class Person(models.Model):
      # Directors and actors

  class BaseContent(models.Model):
      # Abstract base model for movies and series

  class Movie(BaseContent):
      # Movie model

  class Series(BaseContent):
      # Series model
  ```

* **Views (views.py)**

  * `MovieViewSet` and `SeriesViewSet`: API views for listing, searching, and ordering
  * 15-minute caching implemented for performance improvement

* **Tests (tests.py)**

  * Unit tests for listing, searching, and ordering content

* **URLs**

  * `/api/movies/`
  * `/api/series/`
  * Swagger and ReDoc API documentation

---

### 2. Scrapy Scraper

* **Spiders**

  * `NamavaMediaSpider`: Scrapes movie data
  * `NamavaSerialSpider`: Scrapes series data

* **Pipeline (pipeline.py)**

  * Saves scraped data to the database using Django models
  * Automatically manages genres, directors, and actors

---

### 3. Database

* PostgreSQL for relational data storage
* Indexes on `release_year` to improve query performance

---

## ⚙️ Prerequisites

* Python 3.8+
* PostgreSQL 12+
* Redis (for caching)
* Scrapy
* Django and Django REST Framework

---

## 🚀 Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure PostgreSQL Database

Create the database:

```bash
createdb movie_series_db
```

Update database settings in `settings.py`:

```python
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
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Install and Start Redis

```bash
sudo apt-get install redis-server
systemctl start redis
```

### 5. Run the Scraper

To scrape movies:

```bash
scrapy crawl namava_media_spider
```

To scrape series:

```bash
scrapy crawl namava_serial_spider
```

### 6. Start Django Server

```bash
python manage.py runserver
```

---

## 🌐 Access the API

* List movies: `GET /api/movies/`
* Search movies: `GET /api/movies/?search=Inception`
* Order by IMDb rating: `GET /api/movies/?ordering=-imdb`
* List series: `GET /api/series/`
* API Documentation:

  * Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
  * ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 🧪 Running Tests

Run unit tests:

```bash
python manage.py test
```

Tests cover:

* Listing movies and series
* Searching content by title
* Ordering by IMDb rating and release year

---

## ⭐ Key Features

* **Caching:** API responses cached for 15 minutes to boost performance
* **Scraper:** Avoids duplicate data using `processed_ids`
* **Database Optimization:** Indexes used to speed up queries

---

## 🔮 Future Enhancements

* Add authentication to the API
* Support advanced filtering (e.g., by genre)
* Enhance scraper to collect additional data (e.g., posters)

---

