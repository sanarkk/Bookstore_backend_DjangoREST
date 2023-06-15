# Generated by Django 4.1.7 on 2023-06-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainpage", "0004_rename_myuser_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="language",
            field=models.CharField(
                choices=[("en-us", "English"), ("uk", "Ukrainian")],
                default="en-us",
                max_length=7,
            ),
        ),
    ]