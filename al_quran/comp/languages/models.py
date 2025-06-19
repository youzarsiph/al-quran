"""Data Models for al_quran.comp.languages"""

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Language(models.Model):
    """Languages"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text=_("Language name"),
    )
    code = models.CharField(
        max_length=8,
        unique=True,
        db_index=True,
        help_text=_("Language code"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Last update"),
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """Meta data"""

        db_table = "languages"
