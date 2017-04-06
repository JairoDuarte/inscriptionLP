from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils import timezone

class Candidat(models.Model):
    cin = models.CharField(
        _('(CIN)'),
        max_length=50,
        unique=True)
    cne = models.CharField(
        _('(CNE)'),
        max_length=50,
        unique=True)
    nom = models.CharField(
        _('Nom'),
        max_length=100)
    prenom = models.CharField(
        _('Prénom'),
        max_length=100)
    nationalite = models.CharField(
        _('nationalité'),
        max_length=100)
    lieu_naissance = models.CharField(
        _('Pays de nassaince'),
        max_length=100)
    date_nass = models.DateField(
        _('Date naissance'))

    preselection_note = models.DecimalField(
        _('Note Pre-selection'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)

    age_note = models.DecimalField(
        _('Note Âge'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    concours_note = models.DecimalField(
        _('Note concours'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    validation_diplome_note = models.DecimalField(
        _('Validation diplome'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)

    def __str__(self):
        return self.nom + self.prenom

    def preselection_note_(self):
        return 0.25 * self.diplome.moyenne_1_an_() + \
            0.25 * self.diplome.moyenne_2_an_() + \
            0.15 * self.diplomebac.mention.valeur + \
            0.15 * self.age_note + \
            0.20 * self.validation_diplome_note

    def age(self):
        now = timezone.now()
        born = self.date_nass
        return now.year - born.year - \
            ((now.month, now.day) < (born.month, born.day))

    def email(self):
        return self.contacts.email

    def portable_phone(self):
        return self.contacts.portable_phone

    def fixe_phone(self):
        return self.contacts.fixe_phone

    def adresse(self):
        return self.contacts.adresse

    def ville(self):
        return self.contacts.ville

    def pays(self):
        return self.contacts.pays

    class Meta:
        verbose_name_plural = 'candidats'
        db_table = "candidat"
