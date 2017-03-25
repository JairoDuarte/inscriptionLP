from django.forms import ModelForm, inlineformset_factory
from django.forms import formsets
from  django.db import models

from inscription.admin import CandidatAdmin
from inscription.models.Candidat import Candidat
from inscription.models.Contacts import Contacts
from inscription.models.Diplome import Diplome, Bac


class BacFormIn(ModelForm):
    class Meta:
        model = Bac
        fields = '__all__'


class DiplomeFormIn(ModelForm):
    class Meta:
        model = Diplome
        fields = '__all__'


class ContactsFormIn(ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'


class CandidatFormIn(ModelForm):
    class Meta:
        model = Candidat
        fields = '__all__'


"""

CandidatFormSet = formsets.formset_factory(
    Candidat,Contacts,Bac,form=[CandidatFormIn,DiplomeFormIn,], exclude=('candidat','cadidat',)
)


"""