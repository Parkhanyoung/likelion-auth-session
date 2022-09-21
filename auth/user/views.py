from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class PublicUserAPIView(APIView):
  # 인증과 인가를 요구하지 않음(유저 생성이기 때문에)
    permission_classes = []

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        created_user = User.objects.create_user(
            username=username, password=password)
        context = {
            'msg': 'user created',
            'username': created_user.username,
        }
        return Response(context, status.HTTP_201_CREATED)


class ObtainTokenAPIView(APIView):
  # 인증과 인가를 요구하지 않음(최초 토큰 발급이기 떄문)
    permission_classes = []

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        # 인증 실패시
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZATION)

        refresh = RefreshToken.for_user(user)
        context = {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        return Response(context, status=status.HTTP_200_OK)


class UserVerifyAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        console.log(request.user)
        return Response(status=status.HTTP_200_OK)
