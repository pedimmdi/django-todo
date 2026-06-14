from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserRegistrationView, ProfileView
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name ='login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name ='login_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', TokenBlacklistView.as_view(), name='logout')
]
