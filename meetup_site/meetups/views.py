from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm
from .models import Company


class CompanyHome(ListView):
    model = Company
    template_name = 'mysite/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


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


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'mysite/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавления мероприятия'
        return context


class CompanyCategories(ListView):
    model = Company
    template_name = 'mysite/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Company.objects.filter(cat__slug=self.kwargs['cat_slug'])


class ShowPost(DetailView):
    model = Company
    template_name = 'mysite/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context
