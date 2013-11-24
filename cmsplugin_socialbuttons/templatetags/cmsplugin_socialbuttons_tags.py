# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cmsplugin_socialbuttons.models import get_cssclass

register = template.Library()

@register.inclusion_tag('cmsplugin_socialbuttons/button.html')
def render_button(instance, key, title=_('Visit us on %s!')):
    button = instance._meta.get_field(key)
    return {
        'STATIC_URL': settings.STATIC_URL,
        'iconset': getattr(instance, 'iconset', 'MAP_DEFAULT_ICONS'),
        'url': getattr(instance, key),
        'class': instance.get_cssclass(key) or 'foo',
        'title': _(title) % button.verbose_name,
    }

@register.inclusion_tag('cmsplugin_socialbuttons/button.html')
def render_button_with_iconset(instance, key, iconset='MAP_DEFAULT_ICONS', title=_('Visit us on %s!')):
    button = instance._meta.get_field(key)
    return {
        'STATIC_URL': settings.STATIC_URL,
        'iconset': iconset,
        'url': getattr(instance, key),
        'class': get_cssclass(key, iconset),
        'title': _(title) % button.verbose_name,
    }