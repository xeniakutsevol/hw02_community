from django.shortcuts import get_object_or_404, render

from .models import Group, Post


POSTS_PER_PAGE = 10

# Главная страница
def index(request):
    title = "Yatube — главная страница"
    template = "posts/index.html"
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    context = {
        "title": title,
        "posts": posts,
    }
    return render(request, template, context)


# Страница сообщества
def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    title = f"Записи сообщества {group.title}"
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        "title": title,
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
