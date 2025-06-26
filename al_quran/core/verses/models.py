"""Data Models for al_quran.core.verses"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Verse(DateTimeMixin, models.Model):
    """Aayat Al-Quran"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        related_name="verses",
        verbose_name=_("chapter"),
        help_text=_("Verse chapter"),
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="verses",
        verbose_name=_("part"),
        help_text=_("Verse part"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="verses",
        verbose_name=_("group"),
        help_text=_("Verse group"),
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        related_name="verses",
        verbose_name=_("quarter"),
        help_text=_("Verse quarter"),
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        related_name="verses",
        verbose_name=_("page"),
        help_text=_("Verse page"),
    )
    number = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        verbose_name=_("number"),
        help_text=_("Verse number"),
    )
    content = models.CharField(
        max_length=1024,
        db_index=True,
        verbose_name=_("content"),
        help_text=_("Verse content"),
    )

    def __str__(self) -> str:
        return f"{self.chapter.name}, Ayah {self.number}: {self.content[:10]}"

    class Meta:
        """Meta data"""

        db_table = "verses"
        unique_together = ["chapter", "number"]
