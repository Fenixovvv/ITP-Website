from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class HomePageText(models.Model):
    full_text = HTMLField()

    def __str__(self):
        return self.full_text

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=511)
    full_text = HTMLField()
    category = models.CharField(max_length=127)
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(help_text="Check the box if you want the post to appear on the blog page")
    slug = models.CharField(max_length=255, unique=True, help_text="Readable link to the article, example: first_article")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('itpBlog:article_page', kwargs={'slug': self.slug})
