"""файл с конфигурацией приложения"""
from django.apps import AppConfig

class AuthentificationConfig(AppConfig):
    """Файл с конфигурацией приложения. Импортирует сигналы"""
    name = 'authentification'
    def ready(self):
        import authentification.signals.handlers
