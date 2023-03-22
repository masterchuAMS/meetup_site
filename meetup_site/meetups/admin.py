from django.contrib import admin
from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_filter = ('time_create',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Category,CategoryAdmin)