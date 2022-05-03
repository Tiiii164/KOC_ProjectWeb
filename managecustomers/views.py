from django.shortcuts import render, redirect
from django import views

# Create your views here.


def show_customer(request):
    context = {}
    return render(request, "customer/customer.html", context)


def details(request):
    context = {}
    return render(request, "customer/customer.html", context)


def add(request):
    context = {}
    return render(request, "customer/customer.html", context)


def delete(request):
    context = {}
    return redirect(show_customer)


def update(request):
    context = {}
    return render(request, "customer/customer.html", context)


def back_to_list(request):
    return redirect(show_customer)
