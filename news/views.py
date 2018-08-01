from django.shortcuts import render

# Create your views here.
from news.models import Article


def Home(request):
    context = {}
    context['article'] = Article.objects.all().last()
    return render(request, "index.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)
