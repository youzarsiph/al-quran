""" Data Models for quran_api.verses """

from django.db import models


# Create your models here.
class Verse(models.Model):
    """Quran Verses"""

    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text="Verse chapter",
    )
    part = models.ForeignKey(
        "parts.Part",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text="Verse part",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text="Verse group",
    )
    quarter = models.ForeignKey(
        "quarters.Quarter",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text="Verse quarter",
    )
    page = models.ForeignKey(
        "pages.Page",
        on_delete=models.CASCADE,
        related_name="verses",
        help_text="Verse page",
    )
    number = models.IntegerField(
        default=1,
        db_index=True,
        help_text="Verse number",
    )
    text = models.CharField(
        max_length=1024,
        db_index=True,
        help_text="Verse text",
    )

    class Meta:
        """Meta data"""

        unique_together = ["chapter", "number"]
