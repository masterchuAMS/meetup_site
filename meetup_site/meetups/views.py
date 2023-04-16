from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm, RegisterUserForm
from .models import Company
from .utilits import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class CompanyHome(DataMixin, ListView):
    model = Company
    template_name = 'mysite/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(c_def.items())+list(context.items()))


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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'mysite/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавления мероприятия')
        return dict(list(c_def.items()) + list(context.items()))


class CompanyCategories(DataMixin, ListView):
    model = Company
    template_name = 'mysite/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(c_def.items())+list(context.items()))

    def get_queryset(self):
        return Company.objects.filter(cat__slug=self.kwargs['cat_slug'])


class ShowPost(DataMixin, DetailView):
    model = Company
    template_name = 'mysite/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(c_def.items())+list(context.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mysite/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
