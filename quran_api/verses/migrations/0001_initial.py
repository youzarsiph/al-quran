# Generated by Django 5.1 on 2024-11-12 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("chapters", "0001_initial"),
        ("groups", "0001_initial"),
        ("pages", "0001_initial"),
        ("parts", "0001_initial"),
        ("quarters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Verse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        db_index=True, default=1, help_text="Verse number"
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        db_index=True,
                        help_text="Verse content (Arabic)",
                        max_length=1024,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
                (
                    "chapter",
                    models.ForeignKey(
                        help_text="Chapter",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verses",
                        to="chapters.chapter",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="Group",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verses",
                        to="groups.group",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        help_text="Verse page",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verses",
                        to="pages.page",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        help_text="Part",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verses",
                        to="parts.part",
                    ),
                ),
                (
                    "quarter",
                    models.ForeignKey(
                        help_text="Verse quarter",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="verses",
                        to="quarters.quarter",
                    ),
                ),
            ],
            options={
                "unique_together": {("chapter", "number")},
            },
        ),
    ]
