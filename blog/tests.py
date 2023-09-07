from django.test import TestCase
from bs4 import BeautifulSoup
from .models import Post


# Create your tests here.
class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2, 2)

    def test_post_list(self):
        reponse = self.client.get('/blog/')
        self.assertEqual(reponse.status_code, 200)
        soup = BeautifulSoup(reponse.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')
        main_area = soup.find('div', id='main-area')
        self.assertIn(' 게시글이 없습니다 ', main_area.text)
