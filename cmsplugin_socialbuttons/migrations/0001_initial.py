# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialButtons'
        db.create_table('cmsplugin_socialbuttons', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('youtube', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('rss', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('foursquare', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('instagram', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('flickr', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('cmsplugin_socialbuttons', ['SocialButtons'])


    def backwards(self, orm):
        # Deleting model 'SocialButtons'
        db.delete_table('cmsplugin_socialbuttons')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_socialbuttons.socialbuttons': {
            'Meta': {'object_name': 'SocialButtons', 'db_table': "'cmsplugin_socialbuttons'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'flickr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'foursquare': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'rss': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_socialbuttons']