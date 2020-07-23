from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def board(request):
    posts = Post.objects.all()
    return render(request, 'board.html', {'posts':posts})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {'post':post})

def ratings(request):
    return render(request, 'ratings.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')