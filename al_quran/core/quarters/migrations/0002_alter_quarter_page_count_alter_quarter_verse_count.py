# Generated by Django 5.1 on 2025-02-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quarters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quarter",
            name="page_count",
            field=models.PositiveSmallIntegerField(
                db_index=True, default=1, help_text="Number of pages"
            ),
        ),
        migrations.AlterField(
            model_name="quarter",
            name="verse_count",
            field=models.PositiveSmallIntegerField(
                db_index=True, default=1, help_text="Number of verses"
            ),
        ),
    ]
