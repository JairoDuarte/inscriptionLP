from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Age(models.Model):

    max_annee = models.PositiveSmallIntegerField(
        _('Agê'),
        unique=True)
    points = models.DecimalField(
        _('valeur'),
        max_digits=11,
        decimal_places=2)

    def __str__(self):
        return str(self.points) + " - "+str(self.max_annee)

    class Meta:
        verbose_name_plural = 'ages'
        db_table = "age"


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
        db_table = "diplome_annee"


class BacType(models.Model):
    libelle = models.CharField(
        _('libelle'),
        max_length=32)

    def __str__(self):

        return self.libelle

    class Meta:
        verbose_name_plural = 'bactypes'
        db_table = "bactype"


class DiplomeType(models.Model):
    libelle = models.CharField(
        _('libelle'),
        max_length=32)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'diplometypes'
        db_table = "diplometype"


class Mention(models.Model):
    libelle = models.CharField(
        _('libelle'),
        max_length=32)

    valeur = models.DecimalField(
        _('valeur'),
        max_digits=10,
        decimal_places=2)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'mentions'
        db_table = "mention"


class Filiere(models.Model):
    libelle = models.CharField(
        _('libelle'),
        max_length=32)
    responsable = models.CharField(
        _('responsable'),
        max_length=32)
    diplometype = models.ForeignKey(DiplomeType)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'filieres'
        db_table = "filiere"


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
        db_table = "optionfilieres"


class SpecialiteLP(models.Model):
    libelle = models.CharField(
        _('libelle'),
        max_length=32)
    responsable = models.CharField(
        _('responsable'),
        max_length=32)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name_plural = 'specialitelp'
        db_table = "specialitelp"


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
        db_table = "specialite_OPF"