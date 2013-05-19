# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SubParty.logo'
        db.add_column(u'polidata_subparty', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Party.logo'
        db.add_column(u'polidata_party', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SubParty.logo'
        db.delete_column(u'polidata_subparty', 'logo')

        # Deleting field 'Party.logo'
        db.delete_column(u'polidata_party', 'logo')


    models = {
        u'polidata.house': {
            'Meta': {'object_name': 'House'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rol_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polidata.legislative': {
            'Meta': {'object_name': 'Legislative'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roman_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'polidata.legislativepolitician': {
            'Meta': {'object_name': 'LegislativePolitician'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ligislativepolitician_houses'", 'null': 'True', 'to': u"orm['polidata.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'politicians'", 'to': u"orm['polidata.Legislative']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'legislatives'", 'null': 'True', 'to': u"orm['polidata.Party']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'legislatives'", 'to': u"orm['polidata.Politician']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subparty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.SubParty']", 'null': 'True', 'blank': 'True'})
        },
        u'polidata.party': {
            'Meta': {'object_name': 'Party'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polidata.politician': {
            'Meta': {'object_name': 'Politician'},
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'politician_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'profile_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'twitter_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'polidata.subparty': {
            'Meta': {'object_name': 'SubParty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']"})
        }
    }

    complete_apps = ['polidata']