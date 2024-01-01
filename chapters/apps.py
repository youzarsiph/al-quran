""" AppConf for quran_api.chapters """


from django.apps import AppConfig


# Create your config here.
class ChapterConfig(AppConfig):
    """App configuration for quran_api.chapters"""

    name = "quran_api.chapters"
    default_auto_field = "django.db.models.BigAutoField"
