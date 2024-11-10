""" Data Models for quran_api.quarters """

from django.db import models


# Create your models here.
class Quarter(models.Model):
    """Quran Quarters"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return f"Group (Hizb) Quarter {self.pk}"

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a quarter"""

        return self.verses.count()
