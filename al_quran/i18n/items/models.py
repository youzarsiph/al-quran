"""Data Models for al_quran.i18n.items"""

from django.db import models


# Create your models here.
class Item(models.Model):
    """Items"""

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Book",
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items",
        help_text="Chapter",
    )
    verse = models.ForeignKey(
        "verses.Verse",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items",
        help_text="Verse",
    )
    content = models.TextField(
        db_index=True,
        help_text="Content",
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
        return f"{self.book}: {self.chapter if self.chapter else self.verse}"

    class Meta:
        """Meta data"""

        db_table = "items"
