""" Data Models for quran_api.translations """

from django.db import models


# Create your models here.
class Translation(models.Model):
    """Translations"""

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="translations",
        help_text="Language",
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="translations",
        help_text="Chapter",
    )
    verse = models.ForeignKey(
        "verses.Verse",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="translations",
        help_text="Verse",
    )
    content = models.TextField(
        db_index=True,
        help_text="Translation",
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
        return f"{self.language} translation of {self.chapter if self.chapter else self.verse}"

    class Meta:
        """Meta data"""

        db_table = "translations"
