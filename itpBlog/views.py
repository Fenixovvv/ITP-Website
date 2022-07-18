from django.shortcuts import render
from .models import Article

def home_page(request):
    context = {}
    return render(request, "info_page.html", context)

def blog_page(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'blog_page.html', context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article' : article}
    return render(request, 'article_page.html', context)