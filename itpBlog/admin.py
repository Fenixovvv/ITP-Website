from django.contrib import admin
from .models import Article

@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Admin control panel"

