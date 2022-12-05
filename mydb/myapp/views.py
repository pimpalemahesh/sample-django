from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def index(req):
    data = {
        "name": "Mahesh"
    }
    return render(req, "index.html", data)


def about(req):
    return render(req, "about.html")


def contact(req):
    return render(req, "contact.html")


def handleLogin(req):
    if (req.method == "POST"):
        name = req.POST.get('name', 'guest')
        password = req.POST.get('password', 'password')

        user = authenticate(username=name, password=password)
        if user is not None:
            login(name, password)
            messages.success(req, "Successfully loged in...")
            return redirect('contact')
        else:
            messages.error(req, "Invalid credentials")
            return redirect('login')
    return render(req, "login.html")


def handleSignup(req):
    if req.method == "POST":
        username = req.POST.get('name', 'guest')
        signup_email = req.POST.get('email', 'email@gmail.com')
        signup_password = req.POST.get('password', 'password')
        phone = req.POST.get('phone', '111111111')

        myuser = User.objects.create_user(
            username=username, email=signup_email, password=signup_password)
        myuser.phone = phone
        myuser.save()
        messages.success(req, "your account has been successfully created")
        return redirect('about')
    else:
        return render(req, "signup.html")


def signup(req):
    return render(req, "signup.html")


def login(req):
    return render(req, "login.html")
