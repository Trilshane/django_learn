# Generated by Django 5.0.6 on 2024-05-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0002_women_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
