""" Data Models for quran_api.quarters """

from django.db import models


# Create your models here.
class Quarter(models.Model):
    """Arbaa Al-Quran"""

    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="quarters",
        help_text="Group",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Quarter name",
    )
    verse_count = models.IntegerField(
        default=1,
        db_index=True,
        help_text="Number of verses of the chapter",
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
