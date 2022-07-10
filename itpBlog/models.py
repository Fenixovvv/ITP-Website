from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    full_text = models.TextField()
    category = models.CharField(max_length=30)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField()
    # slug = ...(красивая и понятная ссылка на статью)
