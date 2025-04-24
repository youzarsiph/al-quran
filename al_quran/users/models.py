"""Data Models for al_quran.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# Constants
FONTS = [
    ("Amiri", "Amiri"),
    ("font-kufam", "Kufam"),
    ("font-fustat", "Fustat"),
    ("font-reem", "Reem Kufi"),
    ("font-almarai", "Almarai"),
    ("font-cairo", "Cairo Play"),
    ("Amiri Quran", "Amiri Quran"),
    ("font-kufi", "Noto Kufi Arabic"),
    ("font-reem-fun", "Reem Kufi Fun"),
    ("font-noto-ar", "Noto Sans Arabic"),
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
