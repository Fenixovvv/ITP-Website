from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from itpBlog.views import home_page, blog_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('blog/', blog_page, name='blog_page'),
    path('blog/', include(('itpBlog.urls', 'itpBlog'), namespace='itpBlog')),
]
