from datetime import datetime
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from itpBlog.views import blog_page, article_page, home_page
from itpBlog.models import Article


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))
        self.assertIn("<title>Increase The Peace</title>", html)


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
            is_published = True,
            slug = "slug-1"
        )
        article1.save()

        article2 = Article(
            title = "Article II",
            summary = "Summary text II",
            full_text = "Full text II",
            category = "Interview",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True,
            slug = "slug-2"
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
        Article.objects.create(
            title = "Article I",
            summary = "Summary text I",
            full_text = "Full text I",
            category = "News",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True,
            slug = "slug-1"
        )
        Article.objects.create(
            title = "Article II",
            summary = "Summary text II",
            full_text = "Full text II",
            category = "Interview",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True,
            slug = "slug-2"
        )

        request = HttpRequest()
        response = blog_page(request)
        html = response.content.decode("utf8")

        self.assertIn('Article I', html)
        self.assertIn('slug-1', html)
        self.assertIn('Summary text I', html)
        self.assertNotIn('Full text I', html)

        self.assertIn('Article II', html)
        self.assertIn('slug-2', html)
        self.assertIn('Summary text II', html)
        self.assertNotIn('Full text II', html)


class ArticlePageTest(TestCase):

    def test_article_page_displays_correct_article(self):

        Article.objects.create(
            title = "Article I",
            summary = "Summary text I",
            full_text = "Full text I",
            category = "News",
            publication_date = datetime.today().strftime('%Y-%m-%d %H:%M'),
            is_published = True,
            slug = "test-article"
        )

        request = HttpRequest()
        response = article_page(request, "test-article")
        html = response.content.decode("utf8")

        self.assertIn('Article I', html)
        self.assertNotIn('Summary text I', html)
        self.assertIn('Full text I', html)
