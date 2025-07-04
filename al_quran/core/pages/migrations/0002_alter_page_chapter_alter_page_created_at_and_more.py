# Generated by Django 5.2 on 2025-06-26 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chapters", "0003_alter_chapter_created_at_alter_chapter_name_and_more"),
        ("groups", "0002_alter_group_created_at_alter_group_name_and_more"),
        ("pages", "0001_initial"),
        ("parts", "0002_alter_part_created_at_alter_part_name_and_more"),
        ("quarters", "0002_alter_quarter_created_at_alter_quarter_group_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="chapter",
            field=models.ForeignKey(
                help_text="Page chapter",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="chapters.chapter",
                verbose_name="chapter",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, help_text="Date created", verbose_name="Date created"
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="group",
            field=models.ForeignKey(
                help_text="Page group",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="groups.group",
                verbose_name="group",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="name",
            field=models.CharField(
                db_index=True,
                help_text="Page name",
                max_length=16,
                unique=True,
                verbose_name="page name",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="part",
            field=models.ForeignKey(
                help_text="Page part",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="parts.part",
                verbose_name="part",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="quarter",
            field=models.ForeignKey(
                help_text="Page quarter",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="quarters.quarter",
                verbose_name="quarter",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True, help_text="Last update", verbose_name="Last update"
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="verse_count",
            field=models.PositiveSmallIntegerField(
                db_index=True,
                default=1,
                help_text="Number of verses",
                verbose_name="verse count",
            ),
        ),
    ]
