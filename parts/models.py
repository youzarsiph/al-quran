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

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a part (hizb)"""

        return self.verses.count()
