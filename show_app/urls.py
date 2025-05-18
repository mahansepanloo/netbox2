from django.urls import path, include
from rest_framework.routers import DefaultRouter
from show_app.views import MovieViewSet, SeriesViewSet

app_name = "show_app"

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'series', SeriesViewSet, basename='series')

urlpatterns = [
    path("", include(router.urls)),
] + router.urls
