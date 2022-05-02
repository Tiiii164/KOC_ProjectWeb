from django.shortcuts import render, redirect
from django import views

# Create your views here.


def show_home(request):
    return render(request, "cake/home.html")
