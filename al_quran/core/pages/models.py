"""Data Models for al_quran.core.pages"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Page(DateTimeMixin, models.Model):
    """Safahat Al-Quran"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        related_name="pages",
        verbose_name=_("chapter"),
        help_text=_("Page chapter"),
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="pages",
        verbose_name=_("part"),
        help_text=_("Page part"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="pages",
        verbose_name=_("group"),
        help_text=_("Page group"),
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        related_name="pages",
        verbose_name=_("quarter"),
        help_text=_("Page quarter"),
    )
    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        verbose_name=_("page name"),
        help_text=_("Page name"),
    )
    verse_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        verbose_name=_("verse count"),
        help_text=_("Number of verses"),
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """Meta data"""

        db_table = "pages"
