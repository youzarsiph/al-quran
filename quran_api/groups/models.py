""" Data Models for quran_api.groups """

from django.db import models


# Create your models here.
class Group(models.Model):
    """Ahzab Al-Quran"""

    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="groups",
        help_text="Part",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Group name",
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
