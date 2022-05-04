from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from managecustomers.forms import UserForm
# Create your views here.


def show_customer(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "customer/customer.html", context)


def details(request, id):
    # user = User.objects.get(id=id) này là lấy user theo id
    user = get_object_or_404(User, id=id)
    context = {
        "user": user,
    }
    return render(request, "customer/details.html", context)


def add(request):
    forms = UserForm(request.POST or None)

    if forms.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email.password)

        user.save()

        return redirect(show_customer)
    context = {}
    return render(request, "customer/add.html", context)


def delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect(show_customer)


def edit(request, id):
    context = {}
    return render(request, "customer/update.html", context)


def back_to_list(request):
    return redirect(show_customer)
