"""Data Models for al_quran.comp.collections"""

from django.db import models

from al_quran.comp.collections import COLLECTION_TYPES


# Create your models here.
class Collection(models.Model):
    """Collections"""

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="collections",
        help_text="Language",
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=COLLECTION_TYPES,
        help_text="Collection type",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Collection name",
    )
    description = models.CharField(
        max_length=512,
        db_index=True,
        help_text="Collection description",
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
        return f"{self.name} ({self.language})"

    class Meta:
        """Meta data"""

        db_table = "collections"
