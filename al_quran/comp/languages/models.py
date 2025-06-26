"""Data Models for al_quran.comp.languages"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Language(DateTimeMixin, models.Model):
    """Languages"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Language name"),
    )
    code = models.CharField(
        max_length=8,
        unique=True,
        db_index=True,
        verbose_name=_("code"),
        help_text=_("Language code"),
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """Meta data"""

        db_table = "languages"
