# Generated by Django 4.2.5 on 2023-09-17 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_rename_blog_blogs"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogs",
            old_name="name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="blogs",
            name="intro",
        ),
    ]
