from django.db import models
from manageCake.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    DateOfOrder = models.DateTimeField()
    Price = models.FloatField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Order_{str(self.id)} ({str(self.User)})"


class OrderItems(models.Model):
    Quantity = models.IntegerField()
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.Order}_{self.Product}"
