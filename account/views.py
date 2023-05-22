from django.shortcuts import render
from rest_framework import viewsets, status
from account.models import MyUser
from account.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer