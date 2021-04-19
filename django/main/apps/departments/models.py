from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('name'), max_length=200)
    address = models.CharField(_('address'), max_length=255)
    tel = models.CharField(_('tel'), max_length=10)
    website = models.URLField(_('website'))

    class Meta:
        verbose_name = _('Company')

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Department(models.Model):
    company = models.ForeignKey('Company', related_name='+', on_delete=models.CASCADE)
    code = models.CharField(_('code'), max_length=25)
    name = models.CharField(_('name'), max_length=200)

    class Meta:
        verbose_name = _('Department')

    def __str__(self):
        return f'{self.pk}: {self.name}'
