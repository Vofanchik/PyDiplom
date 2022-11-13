from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, UserRegistrSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): #UpdateDestroy
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)