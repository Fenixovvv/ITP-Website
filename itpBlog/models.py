from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    full_text = models.TextField()
    category = models.CharField(max_length=127)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField()
    slug = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('itpBlog:article_page', kwargs={'slug': self.slug})
