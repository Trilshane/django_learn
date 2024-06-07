from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Women, Category, Husband, TagPost, TitleDefault


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "slug",
        "content",
        "photo",
        "post_photo",
        "cat",
        "husband",
        "tags",
        "is_published",
    ]
    readonly_fields = ["post_photo"]
    list_display = (
        "title",
        "post_photo",
        "time_create",
        "is_published",
        "cat",
    )
    list_display_links = ("title",)
    ordering = [
        "time_create",
        "title",
    ]
    list_per_page = 10

    @admin.display(description="Изображение")
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50")
        return "Без Фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    ordering = ["name"]


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
    )
    list_display_links = ("name",)


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ("tag",)
    list_display_links = ("tag",)


@admin.register(TitleDefault)
class TitleDefaultAdmin(admin.ModelAdmin):
    list_display = (
        "title_default",
        "description_default",
        "keywords_default",
    )
    list_display_links = ("title_default",)

    def has_add_permission(self, request):
        return not TitleDefault.objects.exists()
