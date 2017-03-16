from django.contrib import admin

# Register your models here.
from .models.Product import Product
from .models.Category import Category

admin.site.register(Category)
admin.site.register(Product)
