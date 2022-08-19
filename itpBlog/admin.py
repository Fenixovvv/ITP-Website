from django.contrib import admin
from .models import Article, HomePageText

""" @admin.register(Article) """
admin.site.register(Article)
admin.site.register(HomePageText)
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Admin control panel"