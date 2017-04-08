from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from inscription.forms.formsCandidat import *
from inscription.outils.Calcule import CalculeCandidat


def index(request):
    template = loader.get_template('index.html')
    form = CandidatFormIn()

    context = {
    }
    return HttpResponse(template.render(context, request))


def candidatAdd(request):

    if request.method == 'POST':
        form = CandidatFormIn(request.POST)
        formcont = ContactsFormIn(request.POST)
        formdip = DiplomeFormIn(request.POST)
        formbac = BacFormIn(request.POST)

        if form.is_valid() and formcont.is_valid() and formbac.is_valid() and formdip.is_valid():
            candidat = form.save(commit=False)
            candidat.dateAdd = datetime.today()
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

            #creation d'un user pour le candidat
            user = User()
            user.username = candidat.cne
            password = User.objects.make_random_password()
            print(password)
            user.set_password(password)
            user.save()
            print(user.password)
            candidat.user = user
            candidat.save()

            return render(request,'candidat_pdf.html',{"candidat":candidat,"password":password})
        else:
            return render(request, 'inscription.html', context={'form':form, 'formcont':formcont, 'formdip':formdip,'formbac':formbac,'title':'Inscription',})
    else:
        form = CandidatFormIn()
        formcont = ContactsFormIn()
        formdip = DiplomeFormIn()
        formbac = BacFormIn()
        #messages.info(request, "teste")
        context = {
            'title':'Inscription',
            'form':form,
            'formcont':formcont,
            'formdip':formdip,
            'formbac':formbac,
        }
        return render(request,'inscription.html',context)

@login_required
def candidatUpdate(request):

    user = request.user
    try:
        c = user.candidat
    except:
        messages.info(request,"vous n'êtes pas un utilisateur autorisé")
        return render(request,'index.html')
    candidat = user.candidat
    contacts = candidat.contacts
    diplome = candidat.diplome
    bac =candidat.bac

    if request.method == 'POST':
        form = CandidatFormIn(request.POST, instance=candidat)
        formcont = ContactsFormIn(request.POST,instance=contacts)
        formdip = DiplomeFormIn(request.POST,instance=diplome)
        formbac = BacFormIn(request.POST,instance=bac)

        if form.is_valid() and formcont.is_valid() and formbac.is_valid() and formdip.is_valid():
            candidat_ = form.save()
            candidat_.user.username = candidat_.cne
            #user = User.objects.filter(candidat=candidat)
            #user.username = candidat.cne
            diplome_ = formdip.save(commit=False)
            diplome_.moyenne_1_an = CalculeCandidat.moyenne_1(diplome=diplome_)
            diplome_.moyenne_2_an = CalculeCandidat.moyenne_2(diplome=diplome_)
            diplome_.moyenneDiplome = CalculeCandidat.moyenne(diplome=diplome_)
            bac_ = formbac.save()
            formcont.save()
            diplome_.save()
            candidat_.preselection_note = CalculeCandidat.preselection_note(diplome=diplome_,valeur=bac_.mention.valeur)
            candidat_.age_note = CalculeCandidat.age_note(candidat_.age())
            candidat_.validation_diplome_note = CalculeCandidat.validation_diplome(diplome_.nbr_redoublements)
            candidat_.save()
            logout(request)
            messages.success(request, 'Données enregistrées avec succès')
            return render(request,'candidat_pdf.html',{"candidat":candidat})
        else:
            return render(request, 'inscription.html', context={'form':form, 'formcont':formcont, 'formdip':formdip,'formbac':formbac,'title':'modification',})
    else:
        form = CandidatFormIn(instance=candidat)
        formcont = ContactsFormIn(instance=contacts)
        formdip = DiplomeFormIn(instance=diplome)
        formbac = BacFormIn(instance=bac)

        context = {
            'title':'modification',
            'form':form,
            'formcont':formcont,
            'formdip':formdip,
            'formbac':formbac,
        }
        return render(request,'inscription.html',context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    request.session['username'] = user.username
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return redirect(reverse('update'))
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                messages.error(request,"cne et mot de passe incorrect.",)
                return render(request, 'login.html', {'form': form})
        else:
            return render(request,'login.html',{'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

    #JtxMj5ndYL