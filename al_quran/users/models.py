"""Data Models for al_quran.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Constants
FONTS = [
    ("Noto Kufi Arabic", "Noto Kufi Arabic"),
    ("Noto Sans Arabic", "Noto Sans Arabic"),
    ("Reem Kufi Fun", "Reem Kufi Fun"),
    ("Cairo Play", "Cairo Play"),
    ("Fustat", "Fustat"),
    ("Kufam", "Kufam"),
    ("Reem Kufi", "Reem Kufi"),
    ("Almarai", "Almarai"),
    ("Amiri Quran", "Amiri Quran"),
    ("Amiri", "Amiri"),
]

THEMES = [
    ("light", "Light"),
    ("silk", "Light (Silk)"),
    ("lofi", "Light (Simple)"),
    ("caramellatte", "Light (Gold)"),
    ("cupcake", "Light (Lightblue)"),
    ("winter", "Light (Blue)"),
    ("dark", "Dark"),
    ("dim", "Dark (Simple)"),
    ("luxury", "Dark (Gold)"),
    ("night", "Dark (Lightblue)"),
    ("forest", "Dark (Green)"),
    ("sunset", "Dark (Orange)"),
]


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
