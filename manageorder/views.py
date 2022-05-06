from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render, redirect
from managecart.models import CartItems, Cart
from django.contrib.auth.models import User
from manageorder.models import Order, OrderItems
from manageCake.models import Product
from datetime import datetime
# Create your views here.


def show_order(request):
    cart = Cart.objects.get(id=1)

    cart_item = CartItems.objects.filter(Cart=cart)

    if cart_item:
        order=Order()
        order.DateOfOrder = datetime.now()

        order.save()

        for item in cart_item:
            order_item = OrderItems()
            order_item.Product = item.Product
            order_item.Quantity = item.Quantity
            order_item.Price = item.Product.Price
            order_item.Order = order

            order_item.save()
            item.delete()

            context={
                "order_id": order.id,
            }
    return render(request, "order/order.html", context)

