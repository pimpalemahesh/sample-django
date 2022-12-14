from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.handleLogin, name="login"),
    path('signup', views.handleSignup, name="signup")
]
