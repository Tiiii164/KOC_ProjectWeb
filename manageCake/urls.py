from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_home),
    path('detail', views.product_detail),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
]
