"""Data Models for al_quran.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser

from al_quran.users import FONTS, THEMES


# Create your models here.
class User(AbstractUser):
    """Al-Quran Users"""

    font = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=FONTS,
        help_text="Quran Font",
    )
    theme = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=THEMES,
        help_text="App Theme",
    )
    interpretation = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="interpretations",
        help_text="Quran interpretation",
    )
    translation = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="translations",
        help_text="Quran translation",
    )
    transliteration = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transliterations",
        help_text="Quran transliteration",
    )
