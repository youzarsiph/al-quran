"""Data Models for al_quran.comp.collections"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.comp.collections import COLLECTION_TYPES


# Create your models here.
class Collection(models.Model):
    """Collections"""

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="collections",
        help_text=_("Language"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=COLLECTION_TYPES,
        help_text=_("Collection type"),
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text=_("Collection name"),
    )
    description = models.CharField(
        max_length=512,
        db_index=True,
        help_text=_("Collection description"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("Last update"),
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.language})"

    class Meta:
        """Meta data"""

        db_table = "collections"
