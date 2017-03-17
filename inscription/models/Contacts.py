from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _


class Contacts(models.Model):
    email = models.EmailField(
        _('email'),
        max_length=80,
        unique=True)
    portable_phone = models.CharField(
        _('telephone portable'),
        max_length=20,
        unique=True)
    fixe_phone = models.CharField(
        _('telephone fixe'),
        max_length=20,
        blank=True)
    adresse = models.CharField(
        _('adresse de residence'),
        max_length=255)
    ville = models.CharField(
        _('ville de residence'),
        max_length=100)
    pays = models.CharField(
        _('pays de residence'),
        max_length=100)

    def __str__(self):
        return self.adresse + self.ville + "-" + self.pays

    class Meta:
        verbose_name_plural = 'contacts'
        db_table = "contacts"
