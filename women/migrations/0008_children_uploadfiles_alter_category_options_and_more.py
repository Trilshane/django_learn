# Generated by Django 5.0.6 on 2024-06-03 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0007_husband_women_husband"),
    ]

    operations = [
        migrations.CreateModel(
            name="Children",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                ("surname", models.CharField(max_length=255, verbose_name="Фамилия")),
                ("age", models.IntegerField(null=True, verbose_name="Возраст")),
            ],
        ),
        migrations.CreateModel(
            name="UploadFiles",
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
                ("file", models.FileField(upload_to="uploads_model")),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="husband",
            options={"verbose_name": "Партнер", "verbose_name_plural": "Партнеры"},
        ),
        migrations.AlterModelOptions(
            name="women",
            options={
                "verbose_name": "Известные женщины",
                "verbose_name_plural": "Известные женщины",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                db_index=True, max_length=100, verbose_name="Категория"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="husband",
            name="age",
            field=models.IntegerField(null=True, verbose_name="Возраст"),
        ),
        migrations.AlterField(
            model_name="husband",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="women",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="women.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="content",
            field=models.TextField(blank=True, verbose_name="Биография"),
        ),
        migrations.AlterField(
            model_name="women",
            name="husband",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="wuman",
                to="women.husband",
                verbose_name="Муж",
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Статус"),
        ),
        migrations.AlterField(
            model_name="women",
            name="slug",
            field=models.SlugField(max_length=255, unique=True, verbose_name="slug"),
        ),
        migrations.AlterField(
            model_name="women",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="women.tagpost", verbose_name="Теги"
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="time_create",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="women",
            name="time_update",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
        ),
        migrations.AlterField(
            model_name="women",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Имя"),
        ),
    ]