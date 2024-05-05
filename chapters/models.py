""" Data Models for quran_api.chapters """

from django.db import models


# Create your models here.
class Chapter(models.Model):
    """Quran Chapters (Sura)"""

    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        help_text="Chapter name",
    )
    type = models.CharField(
        max_length=8,
        default="Meccan",
        help_text="Designates where the chapter is revealed",
        choices=[("Meccan", "Meccan"), ("Medinan", "Medinan")],
    )
    translation = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Chapter translation",
    )
    transliteration = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Chapter transliteration",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a chapter"""

        return self.verses.count()
