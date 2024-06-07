from typing import Any
from django.db import models
from django.urls import reverse
from uuid import uuid4

from os import path


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="slug"
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Фото",
    )
    content = models.TextField(blank=True, verbose_name="Биография")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Статус")
    cat = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
    )
    tags = models.ManyToManyField(
        "TagPost", blank=True, related_name="tags", verbose_name="Теги"
    )
    husband = models.OneToOneField(
        "Husband",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wuman",
        verbose_name="Муж",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ["-time_create"]

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True, verbose_name="Тэг")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})

    class Meta:
        verbose_name = "Тег категорий"
        verbose_name_plural = "Теги категорий"
        ordering = ["tag"]


class Husband(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(null=True, verbose_name="Возраст")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.name


def path_and_rename(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return path.join(instance.directory_string_var, filename)


class UploadFiles(models.Model):
    directory_string_var = ("uploads_model",)
    file = models.FileField(upload_to=path_and_rename)


class TitleDefault(models.Model):
    title_default = models.CharField(
        max_length=255,
        verbose_name="title страницы по умолчанию",
    )
    description_default = models.CharField(verbose_name="description по умолчанию")
    keywords_default = models.CharField(verbose_name="ключивые слова по умолчанию")

    class Meta:
        verbose_name = "Настройка сайта по умолчанию"
        verbose_name_plural = "Настройки сайта по умолчанию"

    def __str__(self):
        return self.title_default
