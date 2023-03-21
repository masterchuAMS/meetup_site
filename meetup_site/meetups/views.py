from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная свзязь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Company.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'mysite/index.html', context=context)
def about(request):
    return render(request,'mysite/about.html',{'menu':menu,'title':'О сайте'})
def contact(request):
    return render(request, 'mysite/contact.html', {'menu': menu, 'title': 'Контакты'})
def login(request):
    return render(request, 'mysite/login.html', {'menu': menu, 'title': 'Авторизация'})
def show_post(request,post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')
def show_category(request,cat_id):
    posts = Company.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'cats': cats,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'mysite/index.html', context=context)