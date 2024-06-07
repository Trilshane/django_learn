from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator

from .models import Women, Category, TagPost
from .forms import AddPostForm

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

cats_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Певицы"},
    {"id": 3, "name": "Спортсменки"},
]


def index(request):
    posts = Women.objects.filter(is_published=1)
    data = {
        "title": "Главная страница",
        "posts": posts,
        "menu": menu,
        "cat_selected": 0,
    }
    return render(request, "./women/index.html", context=data)


def handle_upload_file(f):
    with open(f"/home/sites/youtube-lesson/uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    objects = Women.objects.order_by("pk")
    contact_list = []
    for obj in objects:
        if obj.is_published:
            contact_list.append(obj)
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "./women/about.html",
        context={"title": "О сайте", "menu": menu, "page_obj": page_obj},
    )


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect("home")
            # except:
            #     form.add_error(None, "Ошибка добавления поста")
            form.save()
            return redirect("home")
    else:
        form = AddPostForm()

    data = {
        "title": "Добавление статьи",
        "menu": menu,
        "form": form,
    }
    return render(
        request,
        "./women/new_post.html",
        context=data,
    )


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(
        Women,
        slug=post_slug,
    )
    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1,
    }
    return render(
        request,
        "women/post.html",
        data,
    )


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)
    cat_url = request.GET.get("cat")
    data = {
        "title": f"Рубрика: {category.name}",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
        "url": cat_url,
    }
    return render(
        request,
        "women/index.html",
        context=data,
    )


def page_not_found(request, exeption):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def new_page_is_found(request):
    return HttpResponse("is new Page")


def show_tag_post_list(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=1)

    data = {
        "title": f"Тег: {tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": None,
    }

    return render(
        request,
        "women/index.html",
        context=data,
    )
