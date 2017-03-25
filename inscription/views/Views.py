from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
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

    context = {
        'categories': Category.objects.all(),
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
        return render(request, 'candidat_form.html', context)
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

        # create a form instance and populate it with data from the request:
        formset = CandidatFormIn(request.POST)
        # check whether it's valid:
        user = request.POST['user']
        return  (request, 'product.html', {'formset': formset, 'user': user})



        if formset.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form


    return render(request,'candidat_form.html')
