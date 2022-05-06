from multiprocessing import context
from django.shortcuts import render
from managecart.models import CartItems, Cart
from django.shortcuts import render, redirect
from manageCake.models import Product
from django.contrib.auth.models import User

# Create your views here.

def remove_from_cart(request, product_id):
    

    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id=1)

    cart_item = CartItems.objects.filter(Product=product, Cart=cart).first()

    if cart_item is not None:   
        cart_item.delete()
    
    return redirect(show_cart)

def show_cart(request):

    if request.method=="POST":
        product = Product.objects.get(id=request.POST["product_id"])
        cart = Cart.objects.get(id=1)
        cart_item = CartItems.objects.filter(Product=product, Cart=cart).first()

        if cart_item is not None:   
            cart_item.Quantity = request.POST["quantity"]
            cart_item.save()
        

    cart = Cart.objects.get(id=1)

    cart_items = CartItems.objects.filter(Cart=cart)

    context={
        "cart_items":cart_items,
    }

    return render(request, "cart/cart.html",context)




