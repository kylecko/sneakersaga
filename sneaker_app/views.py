from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Api, Review
import bcrypt


def index(request):
    return render(request, 'index.html')

# Create your views here.