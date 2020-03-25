from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'

    def ready(self):
        """
        Importing signals module, so they can be invoked
        """
