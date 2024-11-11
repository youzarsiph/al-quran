""" Data Models for quran_api.al_ahzab """

from django.db import models


# Create your models here.
class Hizb(models.Model):
    """Ahzab Al-Quran"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Hizb name",
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
