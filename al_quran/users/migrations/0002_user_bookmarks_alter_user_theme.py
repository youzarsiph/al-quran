# Generated by Django 5.2 on 2025-06-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("verses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bookmarks",
            field=models.ManyToManyField(
                blank=True, help_text="Bookmarks", to="verses.verse"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="theme",
            field=models.CharField(
                blank=True,
                choices=[
                    ("light", "Light"),
                    ("silk", "Light (Silk)"),
                    ("lofi", "Light (Simple)"),
                    ("caramellatte", "Light (Gold)"),
                    ("cupcake", "Light (Cyan)"),
                    ("winter", "Light (Blue)"),
                    ("dark", "Dark"),
                    ("dim", "Dark (Simple)"),
                    ("luxury", "Dark (Gold)"),
                    ("night", "Dark (Cyan)"),
                    ("forest", "Dark (Green)"),
                    ("sunset", "Dark (Orange)"),
                ],
                help_text="App Theme",
                max_length=16,
                null=True,
            ),
        ),
    ]
