from __future__ import unicode_literals
from django.db import models

from .Candidat import Candidat
from .models import Filiere, DiplomeType, Mention, BacType
from django.utils.translation import ugettext as _

class Bac(models.Model):
    candidat = models.OneToOneField(
        Candidat,
        on_delete=models.CASCADE,
        verbose_name=_('candidatBac'),
        )

    date_obtention = models.DateField(
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
        _('semester 1 mark'),
        max_digits=11,
        decimal_places=2)
    s1_an = models.PositiveSmallIntegerField(
        _('semester 1 year'))
    s2_note = models.DecimalField(
        _('semester 2 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s2_an = models.PositiveSmallIntegerField(
        _('semester 2 year'))
    s3_note = models.DecimalField(
        _('semester 3 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s3_an = models.PositiveSmallIntegerField(
        _('semester 3 year'))
    s4_note = models.DecimalField(
        _('semester 4 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    s4_an = models.PositiveSmallIntegerField(
        _('semester 4 year'))
    date_obtention = models.DateField(
        _('date obtention'))
    filiere = models.ForeignKey(Filiere)
    diplometype = models.ForeignKey(DiplomeType)

    type_diplome_autre = models.CharField(
        _('autre type de diplome bac +2'),
        max_length=100,
        blank=True)
    moyenne_1_an = models.DecimalField(
        _('semester 1 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    moyenne_2_an = models.DecimalField(
        _('semester 1 mark'),
        max_digits=11,
        decimal_places=2,
        null=True,
        blank=True)
    moyenneDiplome = models.DecimalField(
        _('semester 1 mark'),
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
