""" Data Models for quran_api.al_aayat """

from django.db import models


# Create your models here.
class Ayah(models.Model):
    """Aayat Al-Quran"""

    sura = models.ForeignKey(
        "as_suwar.Sura",
        on_delete=models.CASCADE,
        related_name="aayat",
        help_text="Sura",
    )
    juz = models.ForeignKey(
        "al_ajzaa.Juz",
        on_delete=models.CASCADE,
        related_name="aayat",
        help_text="Juz",
    )
    hizb = models.ForeignKey(
        "al_ahzab.Hizb",
        on_delete=models.CASCADE,
        related_name="aayat",
        help_text="Hizb",
    )
    riba = models.ForeignKey(
        "al_arbaa.Riba",
        on_delete=models.CASCADE,
        related_name="aayat",
        help_text="Verse quarter",
    )
    safhah = models.ForeignKey(
        "as_safahat.Safhah",
        on_delete=models.CASCADE,
        related_name="aayat",
        help_text="Verse page",
    )
    number = models.IntegerField(
        default=1,
        db_index=True,
        help_text="Ayah number",
    )
    content = models.CharField(
        max_length=1024,
        db_index=True,
        help_text="Ayah content (Arabic)",
    )

    def __str__(self) -> str:
        return f"Surat {self.sura.name}, Ayah {self.number}: {self.content[:20]}"

    class Meta:
        """Meta data"""

        unique_together = ["sura", "number"]
