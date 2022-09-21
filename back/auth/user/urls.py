from django.urls import path
from .views import ObtainTokenAPIView, PublicUserAPIView, UserVerifyAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # 유저 생성
    path('', PublicUserAPIView.as_view()),
    # token 발급
    path('token/', ObtainTokenAPIView.as_view()),
    # Refresh Token을 가지고 Access Token 발급
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    # user 인증 수행
    path('verify/', UserVerifyAPIView.as_view())
]
