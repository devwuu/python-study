from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post, Category
from django.contrib.auth.models import User


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_ddochi = User.objects.create_user(username='ddochi', password='1234')
        self.category_programming = Category.objects.create(name='programming', slug='프로그래밍')
        self.category_music = Category.objects.create(name='music', slug='음악')
        self.post = Post.objects.create(
            title='given',
            content='given content',
            category=self.category_programming,
            author=self.user_ddochi
        )

    def test_post_list(self):
        reponse = self.client.get('/blog/')
        self.assertEqual(reponse.status_code, 200)
        soup = BeautifulSoup(reponse.content, 'html.parser')
        self.assertEqual(soup.title.text, ' Blog ')
        # main_area = soup.find('div', id='main-area')
        # self.assertIn(main_area.text, ' 게시글이 없습니다 ')

    def test_post_detail(self):
        # Creating test database for alias 'default'...
        # 기본으로 테스트용 데이터베이스를 사용하도록 설정되어 있기 때문에
        # given을 꼭 줘야 함

        # given = Post.objects.create(title='given', content='given content', author=self.user_ddochi)
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        post_content = soup.find('p', id='post_content')
        self.assertEqual(self.post.content, post_content.text)

    def test_category_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        find = soup.find('ul', id='categorys')
        self.assertIn(self.category_programming.name, find.text)
