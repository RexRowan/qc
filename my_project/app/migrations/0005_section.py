# Generated by Django 5.0.1 on 2024-01-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_usercontentprogress"),
    ]

    operations = [
        migrations.CreateModel(
            name="Section",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
