from datetime import date, datetime
from unicodedata import category
from django.test import TestCase
from itpBlog.models import Article

class ArticlesTests(TestCase):

    def test_correct_article_model(self):
        # Создание модели статьи
        # Проверка содержимого : название
        # текст предпросмотра, полный текст
        # дата публикации
        article1 = Article(
            title = "Article I",
            summary_text = "Summary text I",
            full_text = "Full text I",
            article_category = "News",
            uploading_date = datetime.today().strftime('%d-%m-%Y')
        )
        article1.save()

        article2 = Article(
            title = "Article II",
            summary_text = "Summary text II",
            full_text = "Full text II",
            article_category = "Interview",
            uploading_date = datetime.today().strftime('%d-%m-%Y')
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