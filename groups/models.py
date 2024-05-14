""" Data Models for quran_api.groups """

from django.db import models


# Create your models here.
class Group(models.Model):
    """Quran Groups (Hizb)"""

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return f"Group (Hizb) {self.pk}"

    @property
    def verse_count(self) -> int:
        """Returns number of verses of a group"""

        return self.verses.count()
