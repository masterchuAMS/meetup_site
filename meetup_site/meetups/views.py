from django.shortcuts import render
from .models import *

menu = ["О сайте","Обратная свзязь","Войти"]
def index(request):
    posts = Company.objects.all()
    return render(request, 'mysite/index.html',{'posts':posts,'menu':menu, 'title':'Главная страница'})
