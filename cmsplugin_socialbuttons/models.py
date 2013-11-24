# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from cmsplugin_socialbuttons.fields import ButtonField

ICON_SETS = (
    ('MAP_DEFAULT_ICONS', 'Default Icons'),
    ('MAP_FONT_AWESOME', 'Font Awesome'),
)

MAP_DEFAULT_ICONS = {
    'facebook': 'facebook',
    'twitter': 'twitter',
    'youtube': 'youtube',
    'googleplus': 'googleplus',
    'rss': 'rss',
    'foursquare': 'foursquare',
    'github': 'github',
    'instagram': 'instagram',
    'flickr': 'flickr',
}

MAP_FONT_AWESOME = {
    'facebook': 'facebook',
    'twitter': 'twitter',
    'youtube': 'youtube',
    'googleplus': 'google-plus',
    'rss': 'rss',
    'foursquare': 'foursquare',
    'github': 'github',
    'instagram': 'instagram',
    'flickr': 'flickr',
}


class SocialButtons(CMSPlugin):
    """Model for social buttons CMS plugin."""

    iconset = models.CharField(_('Icon Set'), choices=ICON_SETS,
                               default='MAP_DEFAULT_ICONS', max_length=100)
    facebook = ButtonField(_('Facebook'))
    twitter = ButtonField(_('Twitter'))
    youtube = ButtonField(_('YouTube'))
    googleplus = ButtonField(_('Google+'))
    rss = ButtonField(_('RSS'))
    foursquare = ButtonField(_('Foursquare'))
    github = ButtonField(_('GitHub'))
    instagram = ButtonField(_('Instagram'))
    flickr = ButtonField(_('Flickr'))

    class Meta:
        verbose_name = _('Social buttons plugin')
        verbose_name_plural = _('Social buttons plugins')

    def __unicode__(self):
        return u'Social buttons'

    def get_cssclass(self, field):
        return get_cssclass(field, self.iconset)


def get_cssclass(field, iconset):
    return globals().get(iconset, {}).get(field, None)