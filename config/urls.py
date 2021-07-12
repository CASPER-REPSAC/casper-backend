from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/boards')),
    path('boards/', include('board.urls')),
    path('accounts/', include('accounts.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
]
