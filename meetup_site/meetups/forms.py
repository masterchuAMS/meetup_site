from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.core.exceptions import ValidationError
from image_uploader_widget.widgets import ImageUploaderWidget

from .models import Company


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Company
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-input'}),
            'slug': forms.Textarea(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-input'}),
        }
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Имя пользователя"}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': "Электронная почта"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': "Подтверждение пароля"}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')