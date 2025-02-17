""" Data Models for al_quran.categories """

from django.db import models


# Create your models here.
class Category(models.Model):
    """Categories"""

    name = models.CharField(
        max_length=32,
        unique=True,
        db_index=True,
        help_text="Category name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Category description",
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
        return self.name

    class Meta:
        """Meta data"""

        db_table = "categories"
