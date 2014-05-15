# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

SUPPORTED_LANGUAGES = [
    ('python', u'Python'),
    ('javascript', u'Python'),
    ('ruby', u'Ruby'),
    ('c#', u'C#'),
    ('c++', u'C++'),
]

class Languages(models.Model):
    name = models.CharField(verbose_name=_('Language'), max_length=255)
    shortcut = models.CharField(verbose_name=_('Shortcut'), max_length=155)

    def __unicode__(self):
        return u"%s (%s)" %(self.name, self.shortcut)


class Tip(models.Model):
    user = models.ForeignKey("accounts.CUser", verbose_name=_("Published by:"))
    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Tip"))
    language = models.ForeignKey("tips.Languages", verbose_name=_("Language"))
    created = models.DateTimeField(_("Created"), auto_created=True)

    def __unicode__(self):
        return u"%s (%s)" %(self.title, self.language)

class VoteManager(models.Manager):
    def get_rating(self):
        return Vote.objects.filter(type=True).count() - Vote.objects.filter(type=False).count()

VOTE_CHOICES = [
    (True, _(u'Positive')),
    (False, _(u'Negative')),
]

class Vote(models.Model):
    type = models.BooleanField(default=False, choices=VOTE_CHOICES)
    user = models.ForeignKey('accounts.CUser', verbose_name=_(u'User'))
    objects = VoteManager()

    def __unicode__(self):
        return u"%s (%s)" %(self.type, self.user)


class Favourite(models.Model):
    user = models.ForeignKey('accounts.CUser', verbose_name=_(u'User'))
    tip = models.ForeignKey('tips.Tip', verbose_name=_('Tip'))

    def __unicode__(self):
        return u"%s (%s)" %(self.tip, self.user)
