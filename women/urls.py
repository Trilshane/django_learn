from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("addpage/", views.add_page, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("post/<slug:post_slug>/", views.show_post, name="post"),
    path("women?category=<slug:cat_slug>/", views.show_category, name="category"),
    path("women?tag=<slug:tag_slug>/", views.show_tag_post_list, name="tag"),
]
