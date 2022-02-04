from django.shortcuts import get_object_or_404, render

from .models import Group, Post


# Главная страница
def index(request):
    title = "Yatube — главная страница"
    template = "posts/index.html"
    posts = Post.objects.order_by("-pub_date")[:10]
    context = {
        "title": title,
        "posts": posts,
    }
    return render(request, template, context)


# Страница сообщества
def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    title = "Записи сообщества " + group.title
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]
    context = {
        "title": title,
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
