from django.apps import AppConfig


class UesrsConfig(AppConfig):
    name = 'uesrs'

    def ready(self):
        import uesrs.signals
