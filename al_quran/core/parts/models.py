"""Data Models for al_quran.core.parts"""

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Part(models.Model):
    """Ajzaa Al-Quran"""

    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        help_text=_("Part name"),
    )
    verse_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text=_("Number of verses"),
    )
    page_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text=_("Number of pages"),
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

        db_table = "parts"
