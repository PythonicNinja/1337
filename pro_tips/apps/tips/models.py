# -*- coding: utf-8 -*-
from django.contrib.comments import Comment
from django.contrib.contenttypes.generic import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

SUPPORTED_LANGUAGES = [
    ('python', u'Python'),
    ('javascript', u'Javascript'),
    ('ruby', u'Ruby'),
    ('c#', u'C#'),
    ('c++', u'C++'),
    ('java', u'Java'),
    ('scala', u'Scala'),
]

class Languages(models.Model):
    name = models.CharField(verbose_name=_('Language'), max_length=255)
    shortcut = models.CharField(verbose_name=_('Shortcut'), max_length=155)
    img = models.ImageField(verbose_name=_('Image'), upload_to="language/", null=True, blank=True)

    def __unicode__(self):
        return u"%s (%s)" %(self.name, self.shortcut)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('index')


class Tip(models.Model):
    user = models.ForeignKey("accounts.CUser", verbose_name=_("Published by:"))
    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Tip"))
    language = models.ForeignKey("tips.Languages", verbose_name=_("Language"))
    created = models.DateTimeField(_("Created"), auto_created=True)
    comments = GenericRelation(Comment, content_type_field='content_type', object_id_field='object_pk')

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
