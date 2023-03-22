from django.db import models
from django.urls import reverse


# Create your models here
class Company(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название Компании')
    content = models.TextField(blank=True, verbose_name='Описание Компании')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Логотип')
    time_create =models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update =models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    class Meta:
        verbose_name = 'It-компании'
        verbose_name_plural = 'It-компании'
        ordering = ['time_create','title']
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Меню')
    url_name= models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.title