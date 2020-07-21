from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

# Create your views here.
def board(request):
    contents = Post.objects.all()
    return render(request, 'board.html', {'post_list':contents})

def detail(request, num):
    post = Post.objects.get(id=num)
    return render(request, 'detail.html', {'result': post})

def new (request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.user = request.user
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('detail', num = post.id)

def update(request, num):
    post = Post.objects.get(id=num)
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('/blog/detail/' + str(post.id))
    return render(request, 'update.html', {'result': post})

def delete(request, num):
    post = Post.objects.get(id=num)
    post.delete()
    return redirect('/')

