""" AppConf for al_quran.books """

from django.apps import AppConfig


# Create your config here.
class BooksConfig(AppConfig):
    """App configuration for al_quran.books"""

    name = "al_quran.books"
    default_auto_field = "django.db.models.BigAutoField"
