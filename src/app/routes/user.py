from django.urls import path

from app.controllers.user.user_api import CustomTokenObtainPairView, CustomTokenRefreshView




urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]