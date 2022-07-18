from django.contrib import admin
from django.urls import path
from itpBlog.views import blog_page, article_page, home_page

app_name = 'itpBlog'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blog/', blog_page, name='blog_page'), 
    path('blog/<slug:slug>/', article_page, name='article_page')  
]
