from django.apps import AppConfig


class ShowAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "show_app"
    def ready(self):
        import show_app.signals