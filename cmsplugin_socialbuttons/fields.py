# -*- coding: utf-8 -*-

from django.db import models

from south.modelsinspector import add_introspection_rules


class ButtonField(models.CharField):
    """A custom button field."""

    def __init__(self, *args, **kwargs):
        self.key = kwargs.pop('key', None)
        kwargs.update({
            'max_length': 200,
            'blank': True,
            'null': True,
        })
        super(ButtonField, self).__init__(*args, **kwargs)


add_introspection_rules([], ['^cmsplugin_socialbuttons.fields.ButtonField'])