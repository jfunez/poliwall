# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'House'
        db.create_table(u'polidata_house', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rol_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'polidata', ['House'])

        # Deleting field 'LegislativePolitician.role'
        db.delete_column(u'polidata_legislativepolitician', 'role')

        # Adding field 'LegislativePolitician.house'
        db.add_column(u'polidata_legislativepolitician', 'house',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='houses', null=True, to=orm['polidata.House']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'House'
        db.delete_table(u'polidata_house')


        # User chose to not deal with backwards NULL issues for 'LegislativePolitician.role'
        raise RuntimeError("Cannot reverse this migration. 'LegislativePolitician.role' and its values cannot be restored.")

        # Deleting field 'LegislativePolitician.house'
        db.delete_column(u'polidata_legislativepolitician', 'house_id')


    models = {
        u'polidata.house': {
            'Meta': {'object_name': 'House'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rol_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'house': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'houses'", 'null': 'True', 'to': u"orm['polidata.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'politicians'", 'to': u"orm['polidata.Legislative']"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']", 'null': 'True', 'blank': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'legislatives'", 'to': u"orm['polidata.Politician']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'})
        },
        u'polidata.subparty': {
            'Meta': {'object_name': 'SubParty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polidata.Party']"})
        }
    }

    complete_apps = ['polidata']