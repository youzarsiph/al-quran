"""Data Models for al_quran.core.pages"""

from django.db import models


# Create your models here.
class Page(models.Model):
    """Safahat Al-Quran"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        related_name="pages",
        help_text="Chapter",
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="pages",
        help_text="Part",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="pages",
        help_text="Group",
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        related_name="pages",
        help_text="",
    )
    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        help_text="Page name",
    )
    verse_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text="Number of verses",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """Meta data"""

        db_table = "pages"
