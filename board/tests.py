from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User
from board.models import Category, Post


class BoardCreateTests(APITestCase):
    def setUp(self):
        User.objects.create_user(email="tester@test.com", password="test1234")
        self.client.login(email="tester@test.com", password="test1234")

    def test_create_category(self):
        """
        Ensure we can create a new category object
        """
        url = reverse('category-list')
        data = {"name": "test category"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "test category")

    def test_create_post(self):
        """
        Ensure we can create a new post object
        """
        category = Category.objects.create(name="category_test")
        category_url = reverse('category-detail', args=[category.pk])
        url = reverse('post-list')
        data = {"category": category_url, "title": "test post", "content": "test post content"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "test post")
        self.assertEqual(Post.objects.get().content, "test post content")
        self.assertEqual(Post.objects.get().viewer_num, 0)


class BoardViewTests(APITestCase):
    def test_view_category_list(self):
        """
        Ensure we can see category objects
        """
        category = Category.objects.create(name="category_test")
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['name'], category.name)

    def test_view_post_list(self):
        """
        Ensure we can see post objects
        """
        user = User.objects.create_user(email="tester@test.com", password="test1234")
        category = Category.objects.create(name="category_test")
        post = Post.objects.create(title="test post", content="test post content", category=category, author=user)
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['title'], post.title)
        self.assertEqual(response.json()[0]['content'], post.content)
        self.assertEqual(response.json()[0]['category'],
                         "http://testserver" + reverse('category-detail', args=[post.category.pk]))
        self.assertEqual(response.json()[0]['viewer_num'], post.viewer_num)
