from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import User
from board.models import Category, Post
from board.serializers import PostSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


class CreateCategoryTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('superuser@test.com', 'superuserpw')
        self.user = User.objects.create_user(email="user@test.com", password="userpw")
        self.category_data = {"name": "test category"}

    def test_superuser_can_create_category(self):
        """
        Ensure superuser can create a new category object
        """
        self.client.login(email="superuser@test.com", password="superuserpw")
        url = reverse('category-list')
        response = self.client.post(url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, self.category_data["name"])

    def test_user_cant_create_category(self):
        """
        Ensure user can't create a new category object
        """
        self.client.login(email="user@test.com", password="userpw")
        url = reverse('category-list')
        response = self.client.post(url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReadCategoryTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="category_test")

    def test_read_category_list(self):
        """
        Ensure we can see category objects list
        """
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['name'], self.category.name)

    def test_read_category_detail(self):
        """
        Ensure we can see a category object detail
        """
        response = self.client.get(reverse('category-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreatePostTests(APITestCase):
    def setUp(self):
        User.objects.create_user(email="user@test.com", password="userpw")
        self.client.login(email="user@test.com", password="userpw")
        self.category = Category.objects.create(name="category_test")
        self.category_url = reverse('category-detail', args=[self.category.pk])
        self.post_data = {"category": self.category_url, "title": "test post", "content": "test post content"}

    def test_create_post(self):
        """
        Ensure we can create a new post object
        """
        url = reverse('post-list')
        response = self.client.post(url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, self.post_data['title'])
        self.assertEqual(Post.objects.get().content, self.post_data['content'])
        self.assertEqual(Post.objects.get().viewer_num, 0)


class ReadPostTests(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(email="user@test.com", password="userpw")
        self.category = Category.objects.create(name="category_test")
        self.post = Post.objects.create(title="test post", content="test post content",
                                        category=self.category, author=self.author)

    def test_read_post_list(self):
        """
        Ensure we can see post objects list
        """
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['title'], self.post.title)
        self.assertEqual(response.json()[0]['content'], self.post.content)
        self.assertEqual(response.json()[0]['category'],
                         "http://testserver" + reverse('category-detail', args=[self.post.category.pk]))
        self.assertEqual(response.json()[0]['viewer_num'], self.post.viewer_num)

    def test_read_post_detail(self):
        """
        Ensure we can see a post object detail
        """
        response = self.client.get(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePostTests(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(email="user@test.com", password="userpw")
        self.client.login(email="user@test.com", password="userpw")
        self.category = Category.objects.create(name="category_test")
        self.post = Post.objects.create(title="test post", content="test post content",
                                        category=self.category, author=self.author)
        factory = APIRequestFactory()
        request = factory.get(reverse('post-detail', args=[self.post.id]))
        serializer_context = {
            'request': Request(request),
        }
        self.post_data = PostSerializer(instance=self.post, context=serializer_context).data
        self.post_data.update({'content': 'Changed'})

    def test_update_post(self):
        """
        Ensure we can update a post object
        """
        response = self.client.put(reverse('post-detail', args=[self.post.id]), self.post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePostTests(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(email="user@test.com", password="userpw")
        self.client.login(email="user@test.com", password="userpw")
        self.category = Category.objects.create(name="category_test")
        self.post = Post.objects.create(title="test post", content="test post content",
                                        category=self.category, author=self.author)

    def test_can_delete_post(self):
        response = self.client.delete(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
