from distutils.text_file import TextFile
from django.db import models
from django.forms import CharField, FloatField

# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.FloatField()
    Image = models.TextField()
    Description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
