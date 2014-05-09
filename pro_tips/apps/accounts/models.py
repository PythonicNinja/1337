# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



USER_MISSION_VERIFICATION = 'can_veryfie_mission'
USER_MISSION_DISACTIVATE = 'can_disactivate_mission'
USER_MISSION_ADD = 'can_add_mission'
USER_MISSION = [
    (USER_MISSION_VERIFICATION, _('Veryfie mission')),
    (USER_MISSION_DISACTIVATE, _('Disactivate mission')),
    (USER_MISSION_ADD, _('Add mission')),
]

USER_PERMISSIONS = tuple(USER_MISSION)


#TODO Languages should be in settings
LANGUAGES = [
    ("en",_("English")),
    ("pl",_("Polish")),
    ("de",_("Germanish ;o")),
]


class CUser(AbstractUser):

    permissions = USER_PERMISSIONS

CUser._meta.get_field('email').blank = False


class CUserProfile(models.Model):
    user = models.ForeignKey('CUser',verbose_name=_("User"))
    language = models.CharField(_("Language"), max_length=2, choices=LANGUAGES)
