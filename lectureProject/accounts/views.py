from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password=request.POST['password1'])
            
            signup = Signup()
            signup.std_num = request.POST['std_num']
            signup.major = request.POST['major']
            signup.name = request.POST['name']
            signup.user = user
            signup.save()
            auth.login(request, user)
            return redirect('home')
    return render(request,'signup.html')    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate (request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')