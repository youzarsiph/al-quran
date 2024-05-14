""" Data Models for quran_api.parts """

from django.db import models


# Create your models here.
class Part(models.Model):
    """Quran Parts (Juz)"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return f"Part (Juz) {self.pk}"

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a part (juz)"""

        return self.verses.count()
