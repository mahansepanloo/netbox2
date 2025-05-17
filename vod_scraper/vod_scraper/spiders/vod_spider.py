import scrapy
import json

class BaseNamavaSpider(scrapy.Spider):
    allowed_domains = ["namava.ir"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processed_ids = set()  

    def parse(self, response):
        try:
            data = json.loads(response.text)
            results = data.get("result", [])
        except json.JSONDecodeError:
            return

        if not results:
            return

        for item in results:
            media_id = item.get("id")
            if media_id:
                preview_url = f"https://www.namava.ir/api/v1.0/medias/{media_id}/preview"
                yield scrapy.Request(url=preview_url, callback=self.parse_preview)

        current_page = int(response.url.split("pi=")[-1].split("&")[0])
        next_page = current_page + 1
        next_url = response.url.replace(f"pi={current_page}", f"pi={next_page}")
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_preview(self, response):
        try:
            data = json.loads(response.text)
            result = data.get("result", {})
        except json.JSONDecodeError:
            return

        source_id = result.get("id")
        if not source_id:
            return

        if source_id in self.processed_ids:
            return

        self.processed_ids.add(source_id)

        yield {
            "source_id": source_id,
            "title": result.get("caption"),
            "lover": result.get("hit"),
            "imdb": result.get("imdb"),
            "year": result.get("year"),
            "story": result.get("story"),
            "director": (
                result.get("director", [{}])[0].get("castName")
                if result.get("director")
                else None
            ),
            "actors": [cast.get("castName") for cast in result.get("casts", [])],
            "categories": [
                cat.get("categoryName") for cat in result.get("categories", [])
            ],
        }

class NamavaMediaSpider(BaseNamavaSpider):
    name = "namava_media_spider"
    content_type = "movie"
    start_urls = [
        "https://www.namava.ir/api/v1.0/category-groups/persian/latest-movies?pi=1&ps=20",
        "https://www.namava.ir/api/v2.0/post-groups/1264/medias?pi=1&ps=20",
        "https://www.namava.ir/api/v1.0/medias/latest-movies?pi=1&ps=20",
    ]

class NamavaSerialSpider(BaseNamavaSpider):
    name = "namava_serial_spider"
    content_type = "series"
    start_urls = [
        "https://www.namava.ir/api/v1.0/category-groups/persian/latest-series?pi=1&ps=20",
        "https://www.namava.ir/api/v2.0/post-groups/1265/medias?pi=1&ps=20",
        "https://www.namava.ir/api/v1.0/category-groups/action/latest-series?pi=1&ps=20",
        "https://www.namava.ir/api/v1.0/category-groups/Thriller/latest-series?pi=1&ps=20"
    ]

