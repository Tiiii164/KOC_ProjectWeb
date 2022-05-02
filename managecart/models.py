from django.db import models
from manageCake.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Cart_" + str(self.User)


class CartItems(models.Model):
    Quantity = models.IntegerField()
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.Cart}_{self.Product}"
