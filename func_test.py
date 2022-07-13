from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging
import unittest

logging.getLogger('WDM').setLevel(logging.NOTSET)

class BasicTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("--disable-gpu")   
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.browser.quit
    
    def test_home_page_title(self):
        # Проверяет текст в заголовке сайта
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("Increase The Peace", self.browser.title)

    def test_home_page_header(self):
        # Проверяет текст в шапке сайта
        self.browser.get("http://127.0.0.1:8000/")
        header = self.browser.find_elements(By.TAG_NAME, "h1")[0]
        self.assertIn("Increase The Peace", header.text)

    def test_blog_list_of_articles(self):
        self.browser.get("http://127.0.0.1:8000/blog/")
        articles_list = self.browser.find_elements(By.CLASS_NAME, "articles-list")
        self.assertTrue(articles_list)

    def test_blog_articles_look_correct(self):
        # Проверяет статью на правильность отображения
        self.browser.get("http://127.0.0.1:8000/blog/")
        article_title = self.browser.find_elements(By.CLASS_NAME, "article-title")
        article_summary = self.browser.find_element(By.CLASS_NAME, "article-summary")
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_blog_article_title_link_leads_to_article_page(self):
        # Переходим на страницу блога
        self.browser.get("http://127.0.0.1:8000/blog/")
        # Ищем название статьи и ссылку на эту статью в тексте названия
        article_title = self.browser.find_elements(By.CLASS_NAME, "article-title")[0]
        article_link = article_title.find_element(By.TAG_NAME, "a")
        article_title_text = article_title.text
        # Переходим по этой ссылке и ищем название статьи
        self.browser.get(article_link.get_attribute("href"))
        article_page_title = self.browser.find_element(By.CLASS_NAME, "article-title")
        # Сравниваем название статьи на главной странице и странице 
        # самой статьи
        self.assertIn(article_title_text, article_page_title.text)



    # Добавить slug(красивые и понятные ссылки на статьи) #TODO
    #
    #
    #
    #

if __name__ == "__main__":
    unittest.main()