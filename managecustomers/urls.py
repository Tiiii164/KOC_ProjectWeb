from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_customer),
    path("/<int:id>", views.details),
    path('/add', views.add),
    path('/delete/<int:id>', views.delete),
    path('/update/<int:id>', views.update),
    path('/back_to_list', views.back_to_list),
]
