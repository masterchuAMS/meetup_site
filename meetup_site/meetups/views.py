from django.http import HttpResponse, Http404
from django.shortcuts import render
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
    return render(request,'mysite/about.html',context=context)
def contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request,'mysite/contact.html', context=context)
def login(request):

    context = {
        'title': 'Войти',
    }
    return render(request, 'mysite/login.html',context=context)
def show_post(request,post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')
def show_category(request,cat_id):
    posts = Company.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'mysite/index.html', context=context)