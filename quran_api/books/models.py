""" Data Models for quran_api.books """

from django.db import models


# Create your models here.
class Book(models.Model):
    """Books"""

    author = models.ForeignKey(
        "authors.Author",
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Author",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Category",
    )
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="books",
        help_text="Language",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Book name",
    )
    description = models.CharField(
        max_length=512,
        db_index=True,
        help_text="Book description",
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
        return f"{self.name} by {self.author} in {self.language}"

    class Meta:
        """Meta data"""

        db_table = "books"
