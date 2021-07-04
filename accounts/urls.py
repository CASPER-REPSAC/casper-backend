from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'appeals', views.AppealViewSet)
router.register(r'activists', views.ActivistViewSet)
router.register(r'observers', views.ObserverViewSet)
router.register(r'rescuers', views.RescuerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('google/login/', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
    path('signup/', views.UserCreate.as_view()),
]
