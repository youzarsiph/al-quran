"""Data Models for al_quran.comp.items"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.mixins.models import DateTimeMixin


# Create your models here.
class Item(DateTimeMixin, models.Model):
    """Items"""

    collection = models.ForeignKey(
        "collections.Collection",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("collection"),
        help_text=_("Item collection"),
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items",
        verbose_name=_("chapter"),
        help_text=_("Item chapter"),
    )
    verse = models.ForeignKey(
        "verses.Verse",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="items",
        verbose_name=_("verse"),
        help_text=_("Item verse"),
    )
    content = models.TextField(
        db_index=True,
        verbose_name=_("content"),
        help_text=_("Item content"),
    )

    def __str__(self) -> str:
        return f"{self.collection}: {self.chapter if self.chapter else self.verse}"

    class Meta:
        """Meta data"""

        db_table = "items"
