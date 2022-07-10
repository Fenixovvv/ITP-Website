from datetime import datetime
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from itpBlog.views import blog_page
from itpBlog.models import Article

class ArticlesTests(TestCase):

    def test_correct_article_model(self):
        # Создание модели статьи
        # Проверка содержимого : название
        # текст предпросмотра, полный текст
        # дата публикации
        # и настройку доступа(публичный/админский)
        article1 = Article(
            title = "Article I",
            summary = "Summary text I",
            full_text = "Full text I",
            category = "News",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True
        )
        article1.save()

        article2 = Article(
            title = "Article II",
            summary = "Summary text II",
            full_text = "Full text II",
            category = "Interview",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True
        )
        article2.save()

        all_articles = Article.objects.all()
        self.assertEqual(len(all_articles), 2)
        
        self.assertEqual(
            all_articles[0].title, 
            article1.title
        )

        self.assertEqual(
            all_articles[1].title, 
            article2.title
        )

    def test_root_url_resolves_to_blog_page(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, blog_page)

    def test_displaying_articles_on_page(self):
        request = HttpRequest()
        response = blog_page(request)
        html = response.content.decode("utf8")

        self.assertIn('title 1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)

        self.assertIn('title 1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)