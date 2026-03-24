from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'index.html')



def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'index.html')#reload page after saving

    return render(request, 'index.html')




#register views
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')

#login views
def login_view(request):
    return render(request, 'login.html')



#logout views
def logout_view(request):
    logout(request)
    return redirect('home')

