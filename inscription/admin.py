from django.contrib import admin

# Register your models here.
# user: admin password:password2017

from .models.Candidat import Candidat
from .models.Contacts import Contacts
from .models.Diplome import Diplome, Bac
from .models.models import BacType, Filiere, OptionFiliere, Age, DiplomeType, DiplomeAnnee
from .models.models import Mention, SpecialiteLP, SpecialiteOptionFiliere


class AgeAdmin(admin.ModelAdmin):
    # ...
    list_display = ('max_annee', 'points')


class ContactsInline(admin.StackedInline):
    model = Contacts


class DiplomeAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Diplome._meta.fields if field.name != "id"]


class DiplomeInline(admin.StackedInline):
    model = Diplome


class BacInline(admin.StackedInline):
    model = Bac


class CandidatAdmin(admin.ModelAdmin):

    inlines = (ContactsInline,BacInline,DiplomeInline,)
    list_display = [field.name for field in Candidat._meta.fields if field.name != "id"] #Candidat._meta.get_fields
    #list_display.append(Candidat.bac)
    #list_display.append(Candidat.contacts)
    """
    for field in Candidat._meta.fields_map:
        for f in  field._meta.fields:
            if f.name != "id":
                list_display.append(f.name)


    """
    for field in Contacts._meta.fields:
         if field.name !="id" and field.name != "candidat":
             list_display.append(field.name)

admin.site.register(Mention)
admin.site.register(Age, AgeAdmin)
admin.site.register(BacType)
admin.site.register(SpecialiteLP)
admin.site.register(DiplomeType)
admin.site.register(DiplomeAnnee)
admin.site.register(Filiere)
admin.site.register(Bac)
admin.site.register(OptionFiliere)
admin.site.register(SpecialiteOptionFiliere)
admin.site.register(Contacts)
admin.site.register(Diplome,DiplomeAdmin)
admin.site.register(Candidat,CandidatAdmin)
admin.AdminSite.site_header = "Gestion des Inscriptions EST Casablanca"
