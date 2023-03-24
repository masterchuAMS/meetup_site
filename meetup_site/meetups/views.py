from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    posts = Company.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'mysite/index.html', context=context)


def about(request):
    context = {
        'title': 'О Сайте',
    }
    return render(request, 'mysite/about.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'mysite/contact.html', context=context)


def login(request):
    context = {
        'title': 'Войти',
    }
    return render(request, 'mysite/login.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Company, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.pk
    }

    return render(request, 'mysite/post.html', context=context)


def show_category(request, cat_slug):
    cat=Category.objects.filter(slug=cat_slug)
    posts = Company.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected':  cat_slug,
    }
    return render(request, 'mysite/index.html', context=context)
