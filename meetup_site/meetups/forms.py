from django import forms
from django.core.exceptions import ValidationError

from .models import Company


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title
