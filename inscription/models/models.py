from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from .Candidat import Candidat
from datetime import date
from .Category import Category

# Create your models here.


class Age(models.Model):
    max_annee = models.PositiveSmallIntegerField(
        _('max age'),
        unique=True)
    points = models.DecimalField(
        _('value'),
        max_digits=11,
        decimal_places=2)
    def __str__(self):
        return self.points
    class Meta:
        verbose_name_plural = 'ages'
        db_table="age"


class DiplomeAnnee(models.Model):
    max_annee = models.PositiveSmallIntegerField(
        _('max age'),
        unique=True)
    points = models.DecimalField(
        _('value'),
        max_digits=11,
        decimal_places=2)
    def __str__(self):
        return self.points

    class Meta:
        verbose_name_plural = 'diplome_annees'
        db_table="diplome_annee"


class BacType(models.Model):
    libelle =models.CharField(
        _('libelle'),
        max_length=32)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'bactypes'
        db_table="bactype"

class DiplomeType(models.Model):
    libelle =models.CharField(
        _('libelle'),
        max_length=32)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'diplometypes'
        db_table="diplometype"


class Mention(models.Model):
    libelle =models.CharField(
        _('libelle'),
        max_length=32)

    interval =models.CharField(
        _('interval'),
        max_length=10)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'mentions'
        db_table="mention"


class Filiere(models.Model):
    libelle =models.CharField(
        _('libelle'),
        max_length=32)
    responsable=models.CharField(
        _('responsable'),
        max_length=32)
    diplome = models.ForeignKey(DiplomeType)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'filiere'
        db_table="filieres"

class OptionFiliere(models.Model):
    libelle = models.CharField(
        _('option filiere'),
        max_length=100,
        unique=True)

    filiere = models.ForeignKey(Filiere)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'optionfiliere'
        db_table="optionfilieres"


class SpecialiteLP(models.Model):
    libelle =models.CharField(
        _('libelle'),
        max_length=32)
    responsable=models.CharField(
        _('responsable'),
        max_length=32)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'specialitelp'
        db_table="specialitelp"


class SpecialiteOptionFiliere(models.Model):
    specialitelp = models.ForeignKey(
        SpecialiteLP,
        on_delete=models.CASCADE,
        verbose_name=_('filierelp'))

    optionFiliere = models.ForeignKey(
        OptionFiliere,
        on_delete=models.CASCADE,
        verbose_name=_('optionfiliere'))

    class Meta:
        verbose_name_plural = 'specialite_OPFs'
        db_table="specialite_OPF"


class Bac(models.Model):
    date_obtention =models.DateField(
        _('date obtention'))
    moyenne = models.FloatField(
        _('moyenne'),
        max_digits=11,
        decimal_places =2)
    mention = models.ForeignKey(Mention)
    typebac = models.ForeignKey(BacType)
    type_bac_autre = models.CharField(
        _('autre type de baccalauréat'),
        max_length=100,
        blank=True)

    def __str__(self):
        return self.bac.libelle

    class Meta:
        verbose_name_plural = 'bacs'
        db_table="bac"
