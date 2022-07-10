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

    def test_news_articles_look_correct(self):
        # Проверяет статью на правильность отображения
        self.browser.get("http://127.0.0.1:8000/news/")
        article_title = self.browser.find_elements(By.CLASS_NAME, "article-title")
        article_summary = self.browser.find_element(By.CLASS_NAME, "article-summary")
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    # Добавить slug(красивые и понятные ссылки на статьи) #TODO
    #
    #
    #
    #

if __name__ == "__main__":
    unittest.main()