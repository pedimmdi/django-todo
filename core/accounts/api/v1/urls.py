from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserRegistrationView, ProfileView


urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name ='login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name ='login_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]
