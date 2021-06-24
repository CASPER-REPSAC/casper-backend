from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
