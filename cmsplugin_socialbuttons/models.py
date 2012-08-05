# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin


class SocialButtons(CMSPlugin):
    """Model for social buttons CMS plugin."""

    facebook = models.CharField(_('Facebook'), blank=True, max_length=200)
    twitter = models.CharField(_('Twitter'), blank=True, max_length=200)
    youtube = models.CharField(_('YouTube'), blank=True, max_length=200)
    googleplus = models.CharField(_('Google+'), blank=True, max_length=200)
    rss = models.CharField(_('RSS'), blank=True, max_length=200)
    foursquare = models.CharField(_('Foursquare'), blank=True, max_length=200)
    github = models.CharField(_('Github'), blank=True, max_length=200)
    instagram = models.CharField(_('Instagram'), blank=True, max_length=200)
    flickr = models.CharField(_('Flickr'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Social buttons plugin')
        verbose_name_plural = _('Social buttons plugins')

    def __unicode__(self):
        return u'Social buttons'
