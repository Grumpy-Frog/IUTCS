# Generated by Django 4.2.5 on 2023-10-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intra_university_event", "0007_remove_intra_university_event_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="intra_university_event",
            name="image",
            field=models.FileField(
                blank=True, null=True, upload_to="intra_event_images"
            ),
        ),
    ]
