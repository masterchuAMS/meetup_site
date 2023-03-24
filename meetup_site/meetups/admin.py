from django.contrib import admin
from .models import *


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url_name')
    list_display_links = ('id', 'title', 'url_name')
    search_fields = ('title', 'url_name')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
