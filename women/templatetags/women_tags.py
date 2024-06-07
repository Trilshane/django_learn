from django import template
import women.views as views
from women.models import Category, TagPost, TitleDefault

register = template.Library()


@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag("women/list_tags.html")
def show_all_tags():
    tags = TagPost.objects.all()
    return {"tags": tags}


@register.inclusion_tag("women/site_title_default.html")
def show_site_default_title():
    settings = TitleDefault.objects.all()[0]
    return {
        "defautl_title": settings.title_default,
    }


@register.inclusion_tag("women/site_description_default.html")
def show_site_default_description():
    settings = TitleDefault.objects.all()[0]
    return {
        "default_description": settings.description_default,
    }


@register.inclusion_tag("women/keywords_default.html")
def show_keywords_default():
    settings = TitleDefault.objects.all()[0]
    return {
        "default_keywords": settings.keywords_default,
    }
