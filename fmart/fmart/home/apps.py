from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    
    #for running the signals django documentation recomends like this
    #after adding here ready(self) method configure the app in settings.py this is important
    #example : home.apps.HomeConfig
    def ready(self):
        import home.signals
