from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from inscription.forms.formsCandidat import *
from inscription.models.Category import Category
from inscription.models.Product import Product

class User:
    def __init__(self,name,year):
        self.name = name
        self.year = year


def index(request):
    template = loader.get_template('index.html')
    form = CandidatFormIn()

    context = {
        'categories': Category.objects.all(),
        'form':form,
    }
    return HttpResponse(template.render(context, request))


def product(request, id):
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))


def addcandidat(request):
    i = ''


def CandidatAdd(request):

    if request.method == 'POST':
        return render(request, 'candidat_form.html')
        form = CandidatFormIn(request.POST)
        formcont = ContactsFormIn(request.POST)
        formdip = DiplomeFormIn(request.POST)
        formbac = BacFormIn(request.POST)
        if form.is_valid() and formcont.is_valid() and formbac.is_valid() and formdip.is_valid():
            #form.save()
            #formcont.save()
            render(request,'index.html')

    else:
        form = CandidatFormIn()
        formcont = ContactsFormIn()
        formdip = DiplomeFormIn()
        formbac = BacFormIn()

    context = {
        'categories': Category.objects.all(),
        'form':form,
        'formcont':formcont,
        'formdip':formdip,
        'formbac':formbac,
    }

    return render(request,'inscription.html',context)


def inscription(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CandidatFormIn(request.POST)
        #if form.is_valid():
          #  i =1
        #else:
         #   return render(request,'index.html',{'form':form})  # (request, 'index.html')


            # create a form instance and populate it with data from the request:
        #formset = CandidatFormIn(request.POST)
        # check whether it's valid:
        #user = request.POST['user']

        # if a GET (or any other method) we'll create a blank form
    return  redirect(reverse('index'))
