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

    def test_post_detail(self):

        # Creating test database for alias 'default'...
        # 기본으로 테스트용 데이터베이스를 사용하도록 설정되어 있기 때문에
        # given을 꼭 줘야 함

        given = Post.objects.create(title='given', content='given content')
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        post_content = soup.find('p', id='post_content')
        self.assertEqual(given.content, post_content.text)
