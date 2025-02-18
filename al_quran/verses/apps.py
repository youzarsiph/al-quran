"""AppConf for al_quran.verses"""

from django.apps import AppConfig


# Create your config here.
class VersesConfig(AppConfig):
    """App configuration for al_quran.verses"""

    name = "al_quran.verses"
    default_auto_field = "django.db.models.BigAutoField"
