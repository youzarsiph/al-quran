""" Data Models for quran_api.pages """

from django.db import models


# Create your models here.
class Page(models.Model):
    """Quran Pages"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pages",
        help_text="Page chapter",
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pages",
        help_text="Page part",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pages",
        help_text="Page group",
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="pages",
        help_text="Page quarter",
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
        return f"Page {self.pk}"

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a chapter"""

        return self.verses.count()
