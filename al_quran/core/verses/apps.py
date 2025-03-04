"""AppConf for al_quran.core.verses"""

from django.apps import AppConfig


# Create your config here.
class VersesConfig(AppConfig):
    """App configuration for al_quran.core.verses"""

    name = "al_quran.core.verses"
    default_auto_field = "django.db.models.BigAutoField"
