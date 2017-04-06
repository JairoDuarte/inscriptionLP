from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from .Candidat import Candidat


class Contacts(models.Model):
    candidat = models.OneToOneField(
        Candidat,
        on_delete=models.CASCADE,
        verbose_name=_('Candidatinfo')
        )
    email = models.EmailField(
        _('Email'),
        max_length=80,
        unique=True)
    portable_phone = models.CharField(
        _('Telephone portable'),
        max_length=20,
        unique=True)
    fixe_phone = models.CharField(
        _('Telephone fixe'),
        max_length=20,
        blank=True)
    adresse = models.CharField(
        _('adresse de résidence'),
        max_length=255)
    ville = models.CharField(
        _('Ville de résidence'),
        max_length=100)
    pays = models.CharField(
        _('pays de résidence'),
        max_length=100)

    def __str__(self):
        return self.adresse + self.ville + "-" + self.pays

    class Meta:
        verbose_name_plural = 'contacts'
        db_table = "contacts"
