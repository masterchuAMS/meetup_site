from meetups.models import Company

class DataMixin:
    paginate_by = 1
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Company.objects.all()
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
