from django.shortcuts import render
from .models import Article

def blog_page(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, "blog_page.html", context)

def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article' : article}
    return render(request, "article_page.html", context)