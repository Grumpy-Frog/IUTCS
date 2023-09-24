# Generated by Django 4.2.5 on 2023-09-24 11:21

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inter_University_Event",
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
                ("title", models.CharField(max_length=100)),
                ("time", models.DateTimeField(blank=True)),
                ("content", mdeditor.fields.MDTextField()),
                (
                    "google_form_link",
                    models.URLField(
                        blank=True, db_index=True, max_length=512, unique=True
                    ),
                ),
            ],
        ),
    ]
