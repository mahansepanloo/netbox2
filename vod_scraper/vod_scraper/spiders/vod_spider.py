import scrapy
import json

class NamavaMediaSpider(scrapy.Spider):
    name = "namava_media_spider"
    allowed_domains = ["namava.ir"]
    start_urls = [
        "https://www.namava.ir/api/v2.0/post-groups/1264/medias?pi=1&ps=20"
    ]

    def parse(self, response):
        data = json.loads(response.text)
        results = data.get("result", [])

        if not results:
            return

        for item in results:
            media_id = item.get("id")
            if media_id:
                preview_url = f"https://www.namava.ir/api/v1.0/medias/{media_id}/preview"
                yield scrapy.Request(
                    url=preview_url,
                    callback=self.parse_preview
                )

        # صفحه بعد
        current_page = int(response.url.split("pi=")[-1].split("&")[0])
        next_page = current_page + 1
        next_url = response.url.replace(f"pi={current_page}", f"pi={next_page}")
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_preview(self, response):
        data = json.loads(response.text)
        result = data.get("result", {})

        yield {
            "source_id": result.get("id"),
            "title": result.get("caption"),
            "lover": result.get("hit"),
            "imdb": result.get("imdb"),
            "year": result.get("year"),
            "story": result.get("story"),
            "director": result.get("director", [{}])[0].get("castName") if result.get("director") else None,
            "actors": [cast.get("castName") for cast in result.get("casts", [])],
            "categories": [cat.get("categoryName") for cat in result.get("categories", [])],
        }
