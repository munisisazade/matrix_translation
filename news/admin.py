from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ('name_az', 'name_ru', 'name_en')


admin.site.register(Article, ArticleAdmin)
