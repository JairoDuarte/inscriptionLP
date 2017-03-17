from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from datetime import date
from .Diplome import Diplome
from .Contacts import Contacts
from .models import SpecialiteLP, Bac


class Candidat(models.Model):
    cin = models.CharField(
        _('national identification code (CIN)'),
        max_length=50,
        unique=True)
    cne = models.CharField(
        _('national student code (CNE)'),
        max_length=50,
        unique=True)
    nom = models.CharField(
        _('first name'),
        max_length=100)
    prenom = models.CharField(
        _('last name'),
        max_length=100)
    nationalite = models.CharField(
        _('nationality'),
        max_length=100)
    lieu_naissance = models.CharField(
        _('birth country'),
        max_length=100)
    date_nass = models.DateField(
        _('birth date'))
    specialitelp = models.ForeignKey(
        SpecialiteLP,
        verbose_name=_('specialitelp'))
    diplome = models.ForeignKey(
        Diplome,
        on_delete=models.CASCADE,
        verbose_name=_('diplome'))
    diplomebac = models.ForeignKey(
        Bac,
        on_delete=models.CASCADE,
        verbose_name=_('degree specialty'),
        null=True,
        blank=True)
    contacts  = models.ForeignKey(
        Contacts,
        on_delete=models.CASCADE,
        verbose_name=_('contacts du candidat'))
    def preselection_mark(self):
        return 0.25 * self.year_1_mark + \
            0.25 * self.year_2_mark + \
            0.15 * self.baccalaureate_rating.value + \
            0.15 * 20 + \
            0.20 * 20
    def age(self):
        now = timezone.now()
        born = self.date_nass
        return now.year - born.year - \
            ((now.month, now.day) < (born.month, born.day))
