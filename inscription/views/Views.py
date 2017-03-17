from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from inscription.models.Category import Category
from inscription.models.Product import Product


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def product(request, cod):
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=cod)
    }
    return HttpResponse(template.render(context, request))
