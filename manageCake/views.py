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


def product_detail(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "cake/detail.html", context)


def add_to_cart(request, product_id):
    return render(request, "cart/cart.html")
