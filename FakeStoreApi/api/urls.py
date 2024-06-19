from api.views.user_view import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include


urlpatterns = [
    path('user/register/', UserRegisterView.as_view(), name='register'),
    path('user/', UserDetailsView.as_view(), name='userOperations'),
    path('token/', TokenObtainPairView.as_view(), name='getToken'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refreshToken'),
    path('auth/', include('rest_framework.urls')),
]
