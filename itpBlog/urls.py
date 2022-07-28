from django.contrib import admin
from django.urls import path
from itpBlog.views import blog_page, article_page, home_page

app_name = 'itpBlog'

urlpatterns = [
    path('blog/<slug:slug>/', article_page, name='article_page'),
]
