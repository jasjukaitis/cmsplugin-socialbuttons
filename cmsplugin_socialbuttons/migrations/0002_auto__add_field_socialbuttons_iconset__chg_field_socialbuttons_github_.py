# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SocialButtons.iconset'
        db.add_column(u'cmsplugin_socialbuttons', 'iconset',
                      self.gf('django.db.models.fields.CharField')(default='MAP_DEFAULT_ICONS', max_length=100),
                      keep_default=False)


        # Changing field 'SocialButtons.github'
        db.alter_column(u'cmsplugin_socialbuttons', 'github', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.instagram'
        db.alter_column(u'cmsplugin_socialbuttons', 'instagram', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.youtube'
        db.alter_column(u'cmsplugin_socialbuttons', 'youtube', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.twitter'
        db.alter_column(u'cmsplugin_socialbuttons', 'twitter', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.googleplus'
        db.alter_column(u'cmsplugin_socialbuttons', 'googleplus', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.foursquare'
        db.alter_column(u'cmsplugin_socialbuttons', 'foursquare', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.facebook'
        db.alter_column(u'cmsplugin_socialbuttons', 'facebook', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.flickr'
        db.alter_column(u'cmsplugin_socialbuttons', 'flickr', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

        # Changing field 'SocialButtons.rss'
        db.alter_column(u'cmsplugin_socialbuttons', 'rss', self.gf('cmsplugin_socialbuttons.fields.ButtonField')(max_length=200, null=True))

    def backwards(self, orm):
        # Deleting field 'SocialButtons.iconset'
        db.delete_column(u'cmsplugin_socialbuttons', 'iconset')


        # Changing field 'SocialButtons.github'
        db.alter_column(u'cmsplugin_socialbuttons', 'github', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.instagram'
        db.alter_column(u'cmsplugin_socialbuttons', 'instagram', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.youtube'
        db.alter_column(u'cmsplugin_socialbuttons', 'youtube', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.twitter'
        db.alter_column(u'cmsplugin_socialbuttons', 'twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.googleplus'
        db.alter_column(u'cmsplugin_socialbuttons', 'googleplus', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.foursquare'
        db.alter_column(u'cmsplugin_socialbuttons', 'foursquare', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.facebook'
        db.alter_column(u'cmsplugin_socialbuttons', 'facebook', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.flickr'
        db.alter_column(u'cmsplugin_socialbuttons', 'flickr', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocialButtons.rss'
        db.alter_column(u'cmsplugin_socialbuttons', 'rss', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_socialbuttons.socialbuttons': {
            'Meta': {'object_name': 'SocialButtons', 'db_table': "u'cmsplugin_socialbuttons'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'facebook': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'flickr': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'foursquare': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'github': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'googleplus': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'iconset': ('django.db.models.fields.CharField', [], {'default': "'MAP_DEFAULT_ICONS'", 'max_length': '100'}),
            'instagram': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rss': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube': ('cmsplugin_socialbuttons.fields.ButtonField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_socialbuttons']