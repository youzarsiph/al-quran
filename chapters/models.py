""" Data Models for quran_api.chapters """

from django.db import models


# Create your models here.
class Chapter(models.Model):
    """Quran Chapters (Sura)"""

    name = models.CharField(
        max_length=16,
        unique=True,
        db_index=True,
        help_text="Chapter name (Arabic)",
    )
    order = models.IntegerField(
        unique=True,
        db_index=True,
        help_text="Refers to the chronological order in which the chapters of the Quran were revealed.",
    )
    type = models.BooleanField(
        default=True,
        help_text="Designates where the chapter is revealed, True means the chapter revealed in Mecca. False means the chapter revealed in Medina",
    )
    verse_count = models.IntegerField(
        db_index=True,
        help_text="Number of verses of the chapter",
    )
    translation = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Chapter translation (English)",
    )
    transliteration = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Chapter transliteration (English)",
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
