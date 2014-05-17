# -*- coding: utf-8 -*-
import logging
from copy import copy

from django.contrib.comments import Comment
from django.contrib.contenttypes.generic import GenericRelation
from django.db import models, IntegrityError
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger("apps.tips")

SUPPORTED_LANGUAGES = [
    ('python', u'Python'),
    ('javascript', u'Javascript'),
    ('ruby', u'Ruby'),
    ('coffee-script', u'Coffee script'),
    ('c#', u'C#'),
    ('c++', u'C++'),
    ('java', u'Java'),
    ('scala', u'Scala'),
]


class Languages(models.Model):
    """
    Languages model for relations

    Creating objects of this model
    >>> l1 = Languages.objects.create(name="test1", shortcut="shortcut1")
    >>> l2 = Languages.objects.create(name="test2", shortcut="shortcut2")

    Test unicode method
    >>> l1.__unicode__()
    'test1 (shortcut1)'
    >>> l2.__unicode__()
    'test1 (shortcut1)'
    """
    name = models.CharField(verbose_name=_('Language'), max_length=255)
    shortcut = models.CharField(verbose_name=_('Shortcut'), max_length=155)
    img = models.ImageField(verbose_name=_('Image'), upload_to="language/", null=True, blank=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.shortcut)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse('index')


class Tip(models.Model):
    user = models.ForeignKey("accounts.CUser", verbose_name=_("Published by:"))
    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Tip"))
    language = models.ForeignKey("tips.Languages", verbose_name=_("Language"))
    created = models.DateTimeField(_("Created"), auto_now=True)
    comments = GenericRelation(Comment, content_type_field='content_type', object_id_field='object_pk')

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.language)

    def get_rating(self):
        return Vote.objects.get_rating_by_tip(self)

    def vote_up(self, user):
        #TODO: !!
        pass

class VoteManager(models.Manager):
    def get_rating_by_tip(self, tip):
        votes = self.filter(tip=tip)
        return votes.filter(type=True).count() - votes.filter(type=False).count()


VOTE_CHOICES = [
    (True, _(u'Positive')),
    (False, _(u'Negative')),
]


class Vote(models.Model):
    type = models.BooleanField(choices=VOTE_CHOICES)
    user = models.ForeignKey('accounts.CUser', verbose_name=_(u'User'))
    tip = models.ForeignKey('tips.Tip', verbose_name=_('Tip'))
    objects = VoteManager()

    def save(self, *args, **kwargs):
        """ used to cast a vote, is assuring if user already voted for this tip allows only
            one vote (up or down)
        """

        if not self.pk:  # only execute if it's a new Vote
            field_names = Vote._meta.get_all_field_names()
            field_names.remove("id")
            fields = dict((f, getattr(self, f)) for f in field_names)

            fields.pop("type")   # ignore type

            user = fields.pop("user")

            possible_vote = None
            try:
                possible_vote = Vote.objects.get(user=user, **fields)
            except Vote.DoesNotExist:
                pass

            if possible_vote:  # user casted already vote on tip
                if self.type != possible_vote.type:
                    # user wants to do an other vote
                    possible_vote.type = self.type
                    return possible_vote.save(update_fields=["type"])
                else:
                    logger.warning('Failed silently: User tried to Vote two times the same Vote')
                    return

        super(Vote, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s (%s)" % (self.type, self.user)


class Favourite(models.Model):
    user = models.ForeignKey('accounts.CUser', verbose_name=_(u'User'))
    tip = models.ForeignKey('tips.Tip', verbose_name=_('Tip'))

    def __unicode__(self):
        return u"%s (%s)" % (self.tip, self.user)
