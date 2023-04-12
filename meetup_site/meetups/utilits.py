from meetups.models import Company

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]
class DataMixin:
    paginate_by = 1
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Company.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] =   0
        return     context
