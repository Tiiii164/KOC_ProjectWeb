from django.shortcuts import render, redirect
from django import views
from manageCake.models import Product

# Create your views here.


def show_home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "cake/home.html", context)
