# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Party'
        db.create_table(u'polidata_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'polidata', ['Party'])

        # Adding model 'SubParty'
        db.create_table(u'polidata_subparty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.Party'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'polidata', ['SubParty'])

        # Adding model 'Legislative'
        db.create_table(u'polidata_legislative', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'polidata', ['Legislative'])

        # Adding model 'Politician'
        db.create_table(u'polidata_politician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('profile_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'polidata', ['Politician'])

        # Adding model 'LegislativePolitician'
        db.create_table(u'polidata_legislativepolitician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('legislative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.Legislative'])),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.Politician'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.Party'], null=True, blank=True)),
            ('subparty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.SubParty'], null=True, blank=True)),
        ))
        db.send_create_signal(u'polidata', ['LegislativePolitician'])


    def backwards(self, orm):
        # Deleting model 'Party'
        db.delete_table(u'polidata_party')

        # Deleting model 'SubParty'
        db.delete_table(u'polidata_subparty')

        # Deleting model 'Legislative'
        db.delete_table(u'polidata_legislative')

        # Deleting model 'Politician'
        db.delete_table(u'polidata_politician')

        # Deleting model 'LegislativePolitician'
        db.delete_table(u'polidata_legislativepolitician')


    models = {
        u'polidata.legislative': {
            'Meta': {'object_name': 'Legislative'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'polidata.legislativepolitician': {
            'Meta': {'object_name': 'LegislativePolitician'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Legislative']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']", 'null': 'True', 'blank': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Politician']"}),
            'subparty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.SubParty']", 'null': 'True', 'blank': 'True'})
        },
        u'polidata.party': {
            'Meta': {'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polidata.politician': {
            'Meta': {'object_name': 'Politician'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'polidata.subparty': {
            'Meta': {'object_name': 'SubParty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']"})
        }
    }

    complete_apps = ['polidata']