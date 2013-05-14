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
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
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
            ('roman_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'polidata', ['Legislative'])

        # Adding model 'Politician'
        db.create_table(u'polidata_politician', (
            ('politician_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='M', max_length=1, db_index=True)),
            ('profile_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('twitter_user', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('profile_id', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'polidata', ['Politician'])

        # Adding model 'House'
        db.create_table(u'polidata_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rol_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'polidata', ['House'])

        # Adding model 'LegislativePolitician'
        db.create_table(u'polidata_legislativepolitician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('legislative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='politicians', to=orm['polidata.Legislative'])),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(related_name='legislatives', to=orm['polidata.Politician'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='legislatives', null=True, to=orm['polidata.Party'])),
            ('subparty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polidata.SubParty'], null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ligislativepolitician_houses', null=True, to=orm['polidata.House'])),
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

        # Deleting model 'House'
        db.delete_table(u'polidata_house')

        # Deleting model 'LegislativePolitician'
        db.delete_table(u'polidata_legislativepolitician')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']"})
        }
    }

    complete_apps = ['polidata']