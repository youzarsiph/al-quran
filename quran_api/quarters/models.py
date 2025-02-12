""" Data Models for quran_api.quarters """

from django.db import models


# Create your models here.
class Quarter(models.Model):
    """Arbaa Al-Quran"""

    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="quarters",
        help_text="Part",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="quarters",
        help_text="Group",
    )
    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        help_text="Quarter name",
    )
    verse_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text="Number of verses",
    )
    page_count = models.PositiveSmallIntegerField(
        default=1,
        db_index=True,
        help_text="Number of pages",
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

        db_table = "quarters"
