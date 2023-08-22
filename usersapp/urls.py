from django.urls import path, include
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'api-users', UserViewSet)

urlpatterns = [
    path('list/', users_list, name='users-list'),
    path('detail/<int:pk>/', user_info, name='users-info'),
    path('players/', PlayerListAPIView.as_view(), name='players'),
    path('user-router/', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authorization/', AuthorizationAPIView.as_view(), name='authorization'),
    path('auth-drf/', AuthDRFAPIView.as_view(), name='auth-drf'),
    path('auth/token/', TokenCreateView.as_view(), name='token_create'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]





