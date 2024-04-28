

from django.apps import AppConfig

class MentalHealthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Mental_Health'

    def ready(self):
        import Mental_Health.signals
