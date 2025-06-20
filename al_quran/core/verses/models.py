"""Data Models for al_quran.core.verses"""

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Verse(models.Model):
    """Aayat Al-Quran"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text=_("Chapter"),
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text=_("Part"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text=_("Group"),
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text=_("Verse quarter"),
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text=_("Verse page"),
    )
    number = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text=_("Verse number"),
    )
    content = models.CharField(
        max_length=1024,
        db_index=True,
        help_text=_("Verse content"),
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
        return f"{self.chapter.name}, Ayah {self.number}: {self.content[:10]}"

    class Meta:
        """Meta data"""

        db_table = "verses"
        unique_together = ["chapter", "number"]
