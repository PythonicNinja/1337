# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings

LANGUAGES = settings.LANGUAGES

class CUser(AbstractUser):
    pass

class CUserProfile(models.Model):
    user = models.ForeignKey('CUser',verbose_name=_("User"))
    language = models.CharField(_("Language"), max_length=2, choices=LANGUAGES)
