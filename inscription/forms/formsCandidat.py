from django.forms import ModelForm, inlineformset_factory, widgets, forms, DateField
from django import forms
from django.forms import formsets
from  django.db import models

from inscription.admin import CandidatAdmin
from inscription.models.Candidat import Candidat
from inscription.models.Contacts import Contacts
from inscription.models.Diplome import Diplome, Bac
from inscription.outils.Calcule import AnneeSemestre
from inscription.outils.Pays import Pays


class BacFormIn(ModelForm):
    class Meta:
        model = Bac
        fields = '__all__'
        exclude =('candidat',)


class DiplomeFormIn(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiplomeFormIn, self).__init__(*args, **kwargs)
        self.fields['s1_an'].widget = widgets.Select(choices=AnneeSemestre.getAnnee())
        self.fields['s2_an'].widget = widgets.Select(choices=AnneeSemestre.getAnnee())
        self.fields['s3_an'].widget = widgets.Select(choices=AnneeSemestre.getAnnee())
        self.fields['s4_an'].widget = widgets.Select(choices=AnneeSemestre.getAnnee())
        self.fields['nbr_redoublements'].widget = widgets.Select(choices=AnneeSemestre.Nbr_Redouble)

    class Meta:
        model = Diplome
        fields = '__all__'
        exclude =('candidat','moyenne_1_an','moyenne_2_an','moyenneDiplome')


class ContactsFormIn(ModelForm):

    def __init__(self, *args, **kwargs):
        # Init parent
        if 'initial' not in kwargs:
            kwargs['initial'] = {
                'pays': 'maroc',
            }
        super(ContactsFormIn, self).__init__(*args, **kwargs)
        self.fields['pays'].widget = widgets.Select(choices=Pays.CHOICES)
        self.fields['adresse'].widget = widgets.Textarea(attrs={'rows': 3})

    class Meta:
        model = Contacts
        fields = '__all__'
        exclude = ('candidat',)

class LoginForm(forms.Form):
    username = forms.CharField(label='CNE', max_length=14)
    password = forms.CharField(widget=forms.PasswordInput())


class CandidatFormIn(ModelForm):

    def __init__(self, *args, **kwargs):
        # Init parent
        if 'initial' not in kwargs:
            kwargs['initial'] = {
                'nationalite': 'maroc',
                'lieu_naissance': 'maroc',
            }
        super(CandidatFormIn, self).__init__(*args, **kwargs)

        self.fields['lieu_naissance'].widget = widgets.Select(choices=Pays.CHOICES)
        self.fields['nationalite'].widget = widgets.Select(choices=Pays.CHOICES)

    class Meta:
        model = Candidat
        fields = '__all__'
        exclude = ('preselection_note', 'age_note', 'concours_note', 'validation_diplome_note', 'user','dateAdd')

class CandidatUpdateFormIn(CandidatFormIn):
    def __init__(self, *args, **kwargs):
        super(CandidatUpdateFormIn, self).__init__(*args, **kwargs)
        self.fields['cin'].disabled = True
        self.fields['cne'].disabled = True
        self.fields['email'].disabled = True

"""

CandidatFormSet = formsets.formset_factory(
    Candidat,Contacts,Bac,form=[CandidatFormIn,DiplomeFormIn,], exclude=('candidat','cadidat',)
)


"""