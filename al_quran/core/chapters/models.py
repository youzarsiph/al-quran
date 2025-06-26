"""Data Models for al_quran.core.chapters"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Chapter(DateTimeMixin, models.Model):
    """Suwar Al-Quran"""

    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Chapter name"),
    )
    order = models.PositiveSmallIntegerField(
        unique=True,
        db_index=True,
        verbose_name=_("order"),
        help_text=_("Chronological order in which chapters were revealed"),
    )
    type = models.BooleanField(
        default=True,
        verbose_name=_("type"),
        help_text=_("Designates where the chapter is revealed"),
        choices=[(True, _("Meccan")), (False, _("Medinan"))],
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

        db_table = "chapters"
