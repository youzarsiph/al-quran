"""Data Models for al_quran.users"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_quran.users import FONTS, THEMES


# Create your models here.
class User(AbstractUser):
    """Al-Quran Users"""

    font = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=FONTS,
        help_text=_("Quran Font"),
    )
    theme = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=THEMES,
        help_text=_("App Theme"),
    )
    interpretation = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="interpretations",
        help_text=_("Quran interpretation"),
        limit_choices_to={"type": 2},
    )
    translation = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="translations",
        help_text=_("Quran translation"),
        limit_choices_to={"type": 0},
    )
    transliteration = models.ForeignKey(
        "collections.Collection",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transliterations",
        help_text=_("Quran transliteration"),
        limit_choices_to={"type": 1},
    )
