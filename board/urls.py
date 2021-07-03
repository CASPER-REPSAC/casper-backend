from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'suggestions', views.SuggestionViewSet)
router.register(r'chats', views.ChatViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
