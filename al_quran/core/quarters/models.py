"""Data Models for al_quran.core.quarters"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Quarter(DateTimeMixin, models.Model):
    """Arbaa Al-Quran"""

    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="quarters",
        verbose_name=_("part"),
        help_text=_("Quarter part"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="quarters",
        verbose_name=_("group"),
        help_text=_("Quarter group"),
    )
    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Quarter name"),
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

        db_table = "quarters"
