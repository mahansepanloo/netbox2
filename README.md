
  🎬 Netbox2
  A Django-powered REST API with Scrapy for scraping and PostgreSQL for storing movie and series data.
  
    
    
    
  



✨ Overview
Netbox2 is a sleek and modern RESTful API built with Django, integrated with Scrapy for web scraping, and powered by PostgreSQL. It scrapes movie and series data from Namava.ir, stores it efficiently, and provides robust endpoints for querying with filtering, ordering, and caching.
🚀 Features

🕷️ Web Scraping: Extracts movie/series details (title, year, genres, directors, actors, IMDb, etc.) from Namava.ir.
🌐 REST API: Query movies and series with search and sorting capabilities.
🗄️ Database: Structured PostgreSQL storage for genres, persons, movies, and series.
⚡ Caching: 15-minute response caching for optimized performance.
📜 API Docs: Interactive Swagger and ReDoc interfaces.

📂 Project Structure
netbox2/
├── manage.py
├── show_app/
│   ├── migrations/
│   ├── models.py          # 📋 Database models
│   ├── serializers.py     # 🔄 API serializers
│   ├── urls.py           # 🔗 App URLs
│   ├── views.py          # 👁️ API viewsets
│   └── pipelines.py      # 🛠️ Scrapy pipeline
├── vod_scraper/
│   ├── spiders/
│   │   └── namava_spider.py  # 🕸️ Scrapy spiders
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── netbox2/
│   ├── settings.py
│   ├── urls.py           # 🌍 Root URLs
│   ├── asgi.py
│   └──–

 wsgi.py
├── requirements.txt
└── README.md

🛠️ Requirements

🐍 Python 3.8+
🐘 PostgreSQL 13+
🌟 Django 4.x
🔗 Django REST Framework
🕷️ Scrapy
📖 drf-yasg (Swagger/ReDoc)
🔌 psycopg2 (PostgreSQL adapter)

Install dependencies:
pip install -r requirements.txt

📚 Setup Instructions
1. Clone the Repository
git clone https://github.com/your-repo/netbox2.git
cd netbox2

2. Configure Environment
Create a .env file:
DATABASE_URL=postgresql://username:password@localhost:5432/netbox2
SECRET_KEY=your-django-secret-key
DEBUG=True

3. Set Up PostgreSQL
Create the database:
CREATE DATABASE netbox2;

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Run Scrapy Spiders
Scrape movies:
scrapy crawl namava_media_spider

Scrape series:
scrapy crawl namava_serial_spider

6. Start the Server
python manage.py runserver

Access the API at: http://localhost:8000/api/
7. Explore API Documentation

📖 Swagger UI: http://localhost:8000/swagger/
📄 ReDoc: http://localhost:8000/redoc/

🌐 API Endpoints
🎥 Movies

List: GET /api/movies/
🔍 search: Filter by title/genre (e.g., ?search=action)
📅 ordering: Sort by release_year or imdb (e.g., ?ordering=-imdb)


Retrieve: GET /api/movies/<source_id>/

📺 Series

List: GET /api/series/
🔍 search: Filter by title/genre
📅 ordering: Sort by release_year or imdb


Retrieve: GET /api/series/<source_id>/

🕷️ Scrapy Spiders

NamavaMediaSpider: Scrapes movie data.
NamavaSerialSpider: Scrapes series data.
Both paginate through Namava.ir APIs, extracting unique entries by source_id.

🗄️ Database Models

Genre: Unique genre names.
Person: Directors and actors.
BaseContent: Abstract model for shared fields (title, year, etc.).
Movie/Series: Inherit from BaseContent.

⚡ Caching
API responses are cached for 15 minutes using cache_page.
🧪 Running Tests
python manage.py test

🛠️ Troubleshooting

Database Errors: Check PostgreSQL status and DATABASE_URL.
Scrapy Issues: Review logs for network/JSON errors.
API Problems: Use Swagger for endpoint details.

🤝 Contributing

Fork the repo.
Create a branch: git checkout -b feature-name
Commit: git commit -m "Add feature"
Push: git push origin feature-name
Open a pull request.

📜 License
Licensed under the MIT License.


  Built with ❤️ using Django, Scrapy, and PostgreSQL
