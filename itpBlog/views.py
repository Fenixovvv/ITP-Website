from django.shortcuts import render
from .models import Article, HomePageText

def home_page(request):
    text = HomePageText.objects.all()[0].full_text
    context = {'text' : text}
    return render(request, 'info_page.html', context)

def blog_page(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'blog_page.html', context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article' : article}
    return render(request, 'article_page.html', context)
