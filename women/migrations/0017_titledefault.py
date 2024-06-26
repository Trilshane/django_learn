# Generated by Django 5.0.6 on 2024-06-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0016_alter_tagpost_options_alter_women_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="TitleDefault",
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
                (
                    "title_default",
                    models.CharField(
                        max_length=255, verbose_name="title страницы по умолчанию"
                    ),
                ),
                (
                    "meta_tags_default",
                    models.CharField(verbose_name="мета теги по умолчанию"),
                ),
            ],
        ),
    ]
