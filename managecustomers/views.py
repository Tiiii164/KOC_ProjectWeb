from django.shortcuts import render, redirect
from django import views

# Create your views here.


def show_customer(request):
    context = {}
    return render(request, "customer/customer.html", context)
