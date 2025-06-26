"""Data Models for al_quran.core.parts"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Part(DateTimeMixin, models.Model):
    """Ajzaa Al-Quran"""

    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Part name"),
    )
    verse_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        verbose_name=_("verse count"),
        help_text=_("Number of verses"),
    )
    page_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        verbose_name=_("page count"),
        help_text=_("Number of pages"),
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """Meta data"""

        db_table = "parts"
