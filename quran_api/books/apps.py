""" AppConf for quran_api.books """

from django.apps import AppConfig


# Create your config here.
class BooksConfig(AppConfig):
    """App configuration for quran_api.books"""

    name = "quran_api.books"
    default_auto_field = "django.db.models.BigAutoField"
