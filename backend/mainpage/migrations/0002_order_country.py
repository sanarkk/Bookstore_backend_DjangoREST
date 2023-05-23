# Generated by Django 4.1.7 on 2023-05-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainpage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="country",
            field=models.CharField(
                choices=[("CA", "Canada"), ("UA", "Ukraine")],
                default="UA",
                max_length=2,
            ),
        ),
    ]