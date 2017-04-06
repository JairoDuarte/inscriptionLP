from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from inscription.forms.formsCandidat import *
from inscription.outils.Calcule import CalculeCandidat


class User:
    def __init__(self,name,year):
        self.name = name
        self.year = year


def index(request):
    template = loader.get_template('index.html')
    form = CandidatFormIn()

    context = {
    }
    return HttpResponse(template.render(context, request))



def addcandidat(request):
    i = ''


def CandidatAdd(request):

    if request.method == 'POST':
        form = CandidatFormIn(request.POST)
        formcont = ContactsFormIn(request.POST)
        formdip = DiplomeFormIn(request.POST)
        formbac = BacFormIn(request.POST)
        t = form.is_valid()
        k = formbac.is_valid()
        c = formcont.is_valid()
        d = formdip.is_valid()

        if form.is_valid() and formcont.is_valid() and formbac.is_valid() and formdip.is_valid():
            candidat = form.save(commit=False)
            candidat.save()
            diplome = formdip.save(commit=False)
            diplome.moyenne_1_an = CalculeCandidat.moyenne_1(diplome=diplome)
            diplome.moyenne_2_an = CalculeCandidat.moyenne_2(diplome=diplome)
            diplome.moyenneDiplome = CalculeCandidat.moyenne(diplome=diplome)
            bac = formbac.save(commit=False)
            contacts = formcont.save(commit=False)
            contacts.candidat =candidat
            contacts.save()
            diplome.candidat = candidat
            diplome.save()
            bac.candidat = candidat
            bac.save()
            candidat.preselection_note = CalculeCandidat.preselection_note(diplome=diplome,valeur=bac.mention.valeur)
            candidat.age_note = CalculeCandidat.age_note(candidat.age())
            candidat.validation_diplome_note = CalculeCandidat.validation_diplome(diplome.nbr_redoublements)
            candidat.save()

            return render(request,'index.html')
            # form.save()
            # formcont.save()
        else:
            return render(request, 'inscription.html', context={'form':form, 'formcont':formcont, 'formdip':formdip,'formbac':formbac,})
    else:
        form = CandidatFormIn()
        formcont = ContactsFormIn()
        formdip = DiplomeFormIn()
        formbac = BacFormIn()

        context = {
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
