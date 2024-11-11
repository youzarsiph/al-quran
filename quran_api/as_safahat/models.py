""" Data Models for quran_api.as_safahat """

from django.db import models


# Create your models here.
class Safhah(models.Model):
    """Safahat Al-Quran"""

    sura = models.ForeignKey(
        "as_suwar.Sura",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="safahat",
        help_text="Sura",
    )
    juz = models.ForeignKey(
        "al_ajzaa.Juz",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="safahat",
        help_text="Juz",
    )
    hizb = models.ForeignKey(
        "al_ahzab.Hizb",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="safahat",
        help_text="Hizb",
    )
    riba = models.ForeignKey(
        "al_arbaa.Riba",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="safahat",
        help_text="",
    )
    verse_count = models.IntegerField(
        default=1,
        db_index=True,
        help_text="Number of verses of the chapter",
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
