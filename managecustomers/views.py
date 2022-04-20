from django.shortcuts import render, redirect
from django import views

# Create your views here.


def show_customer(request):
    return render(request, "customers/customer.html")
