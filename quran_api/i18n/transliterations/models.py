""" Data Models for quran_api.i18n.transliterations """

from django.db import models


# Create your models here.
class Transliteration(models.Model):
    """Transliterations"""

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="transliterations",
        help_text="Language",
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="transliterations",
        help_text="Chapter",
    )
    verse = models.ForeignKey(
        "verses.Verse",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="transliterations",
        help_text="Verse",
    )
    content = models.TextField(
        db_index=True,
        help_text="Transliteration",
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
        return f"{self.language} transliteration of {self.chapter if self.chapter else self.verse}"

    class Meta:
        """Meta data"""

        db_table = "transliterations"
