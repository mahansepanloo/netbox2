from show_app.models import Movie, Series, Genre, Person
from twisted.internet.threads import deferToThread
from django.db import transaction

class NamavaPipeline:
    def process_item(self, item, spider):
        return deferToThread(self._save_item, item, spider)

    @transaction.atomic
    def _save_item(self, item, spider):
        model = Movie if spider.content_type == "movie" else Series

        obj, created = model.objects.get_or_create(
            source_id=item["source_id"],
            defaults={
                "title": item.get("title"),
                "release_year": item.get("year"),
                "lover": item.get("lover"),
                "imdb": item.get("imdb"),
                "story": item.get("story"),
            },
        )

        # ژانرها
        for genre_name in item.get("categories", []):
            genre, _ = Genre.objects.get_or_create(name=genre_name)
            obj.genres.add(genre)

        # کارگردان‌ها
        if item.get("director"):
            director, _ = Person.objects.get_or_create(name=item["director"])
            obj.directors.add(director)

        # بازیگران
        for actor_name in item.get("actors", []):
            actor, _ = Person.objects.get_or_create(name=actor_name)
            obj.actors.add(actor)

        return item
