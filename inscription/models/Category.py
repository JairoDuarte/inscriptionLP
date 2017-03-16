from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
