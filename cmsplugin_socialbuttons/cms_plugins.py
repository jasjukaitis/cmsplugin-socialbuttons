# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_socialbuttons import models


class SocialButtonsPlugin(CMSPluginBase):
    """Social buttons CMS plugin."""

    name = _('Social buttons')
    model = models.SocialButtons
    render_template = 'cmsplugin_socialbuttons/list.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(SocialButtonsPlugin)
