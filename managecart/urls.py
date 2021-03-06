from sys import path_hooks
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_cart),
    path('cart/remove_from_cart/<int:product_id>', views.remove_from_cart),
]
