from __future__ import unicode_literals
from django.db import models
from .models import Filiere,DiplomeType
from django.utils.translation import ugettext as _


class Diplome(models.Model):

    s1_note = models.FloatField(
        _('semester 1 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s1_an = models.PositiveSmallIntegerField(
        _('semester 1 year'))
    s2_note = models.FloatField(
        _('semester 2 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s2_an = models.PositiveSmallIntegerField(
        _('semester 2 year'))
    s3_note = models.FloatField(
        _('semester 3 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s3_an = models.PositiveSmallIntegerField(
        _('semester 3 year'))
    s4_note = models.FloatField(
        _('semester 4 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s4_an = models.PositiveSmallIntegerField(
        _('semester 4 year'))

    date_obtention =models.DateField(
        _('date obtention'))
    filiere = models.ForeignKey(Filiere)
    diplome = models.ForeignKey(DiplomeType)

    type_diplome_autre = models.CharField(
        _('autre type de diplome bac +2'),
        max_length=100,
        blank=True)

    def __str__(self):
        return str(self.diplome.libelle+" "+self.filiere.libelle)

    def moyenne_1_an(self):
        return (self.s1_note+self.s2_note)/2

    def moyenne_2_an(self):
        return (self.s3_note + self.s4_note) / 2

    def moyenne(self):
        return (self.moyenne_1_an() + self.moyenne_2_an()) / 2



