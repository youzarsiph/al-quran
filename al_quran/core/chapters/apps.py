"""AppConf for al_quran.core.chapters"""

from django.apps import AppConfig


# Create your config here.
class ChaptersConfig(AppConfig):
    """App configuration for al_quran.core.chapters"""

    name = "al_quran.core.chapters"
    default_auto_field = "django.db.models.BigAutoField"
