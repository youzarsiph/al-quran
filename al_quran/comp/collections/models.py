"""Data Models for al_quran.comp.collections"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.comp.collections import COLLECTION_TYPES
from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Collection(DateTimeMixin, models.Model):
    """Collections"""

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="collections",
        verbose_name=_("language"),
        help_text=_("Collection Language"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=COLLECTION_TYPES,
        verbose_name=_("type"),
        help_text=_("Collection type"),
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Collection name"),
    )
    description = models.CharField(
        max_length=512,
        db_index=True,
        verbose_name=_("description"),
        help_text=_("Collection description"),
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.language})"

    class Meta:
        """Meta data"""

        db_table = "collections"
