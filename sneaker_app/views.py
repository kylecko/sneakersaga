from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Sneaker, Review
import bcrypt

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Sneaker, Review
from .serializers import UserSerializer, SneakerSerializer, ReviewSerializer


def index(request):
    return render(request, 'index.html')


class UserViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SneakerViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = SneakerSerializer
    queryset = Sneaker.objects.all()


class ReviewViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

# Create your views here.
