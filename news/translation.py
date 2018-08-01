from modeltranslation.translator import translator, TranslationOptions
from .models import Article


class ArticleTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Article, ArticleTranslationOptions)
