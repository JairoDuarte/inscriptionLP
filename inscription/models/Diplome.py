from __future__ import unicode_literals
from django.db import models

from .Candidat import Candidat
from .models import Filiere, DiplomeType, Mention, BacType, SpecialiteLP
from django.utils.translation import ugettext as _

class Bac(models.Model):
    candidat = models.OneToOneField(
        Candidat,
        on_delete=models.CASCADE,
        verbose_name=_('candidatBac'),
        )

    date_obtention_bac = models.DateField(
        _('date obtention'))
    moyenne = models.DecimalField(
        _('moyenne'),
        max_digits=11,
        decimal_places=2)
    mention = models.ForeignKey(Mention)
    typebac = models.ForeignKey(BacType)
    type_bac_autre = models.CharField(
        _('autre type de baccalauréat'),
        max_length=100,
        blank=True)

    def __str__(self):
        return self.typebac.libelle

    class Meta:
        verbose_name_plural = 'bacs'
        db_table = "bac"


class Diplome(models.Model):
    candidat = models.OneToOneField(
        Candidat,
        on_delete=models.CASCADE,
        verbose_name=_('candidatdiplome'))

    s1_note = models.DecimalField(
        _('Note S1'),
        max_digits=11,
        decimal_places=2)
    s1_an = models.CharField(
        _('Année S1'),
        max_length=10)
    s2_note = models.DecimalField(
        _('Note S2'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s2_an =models.CharField(
        _('Année S2'),
        max_length=10)
    s3_note = models.DecimalField(
        _('Note S3'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s3_an = models.CharField(
        _('Année S3'),
        max_length=10)

    s4_note = models.DecimalField(
        _('Note S4'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s4_an = models.CharField(
        _('Année S4'),
        max_length=10)

    date_obtention_dip = models.DateField(
        _('date obtention'))

    nbr_redoublements = models.DecimalField(
        _('Nbr de redouble'),
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True)

    diplometype = models.ForeignKey(DiplomeType)

    type_diplome_autre = models.CharField(
        _('autre type de diplome'),
        max_length=100,
        blank=True)
    filiere = models.ForeignKey(Filiere)

    specialitelp = models.ForeignKey(
        SpecialiteLP,
        verbose_name=_('Specialité LP'))

    moyenne_1_an = models.DecimalField(
        _('moyenne 1 année'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    moyenne_2_an = models.DecimalField(
        _('moyenne 2 année'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    moyenneDiplome = models.DecimalField(
        _('moyenne diplome'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)

    def __str__(self):
        return str(self.diplometype.libelle+" "+self.filiere.libelle)

    def moyenne_1_an_(self):
        return (self.s1_note+self.s2_note)/2

    def moyenne_2_an_(self):
        return (self.s3_note + self.s4_note) / 2

    def moyennediplome_(self):
        return (self.moyenne_1_an_() + self.moyenne_2_an_()) / 2

    class Meta:
        verbose_name_plural = 'diplomes'
        db_table = "diplome"
