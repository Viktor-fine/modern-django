#from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    #""" Конечная точка API позволяющая просматривать или редактировать пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

