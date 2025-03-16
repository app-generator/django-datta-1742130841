# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Hecho_Extraordinario(models.Model):

    #__Hecho_Extraordinario_FIELDS__
    oace = models.TextField(max_length=255, null=True, blank=True)
    osde = models.TextField(max_length=255, null=True, blank=True)
    entidad = models.TextField(max_length=255, null=True, blank=True)
    clasificación = models.TextField(max_length=255, null=True, blank=True)
    descripción = models.TextField(max_length=255, null=True, blank=True)

    #__Hecho_Extraordinario_FIELDS__END

    class Meta:
        verbose_name        = _("Hecho_Extraordinario")
        verbose_name_plural = _("Hecho_Extraordinario")



#__MODELS__END
