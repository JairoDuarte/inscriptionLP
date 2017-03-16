from __future__ import unicode_literals
from django.db import models

# Create your models here.
from .Category import Category

class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return  self.name

