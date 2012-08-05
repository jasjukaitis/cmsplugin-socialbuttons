# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.inclusion_tag('cmsplugin_socialbuttons/button.html')
def render_button(button, url, cssclass, title=_('Visit us on %s!')):
    return {
        'button': button,
        'STATIC_URL': settings.STATIC_URL,
        'url': url,
        'class': cssclass,
        'title': _(title) % button,
    }
