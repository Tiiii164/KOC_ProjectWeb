from django.shortcuts import render, redirect
from django import views
from manageCake.models import Product
from managecart.models import CartItems, Cart
from django.contrib.auth.models import User
from managecart import views
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
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id=1)
    cart_item = CartItems()
    cart_item.Product = product
    cart_item.Cart = cart
    cart_item.Quantity = 1
    cart_item.save()

    return redirect(request, views.show_cart)
