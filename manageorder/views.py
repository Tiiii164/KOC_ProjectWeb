from django.shortcuts import render
from manageCake.models import Product
# Create your views here.


def show_order(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "order/order.html", context)
