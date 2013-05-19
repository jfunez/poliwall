# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PoliticianSalary'
        db.create_table(u'polisalary_politiciansalary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(related_name='salaries', to=orm['polidata.Politician'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'polisalary', ['PoliticianSalary'])


    def backwards(self, orm):
        # Deleting model 'PoliticianSalary'
        db.delete_table(u'polisalary_politiciansalary')


    models = {
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
        u'polisalary.politiciansalary': {
            'Meta': {'object_name': 'PoliticianSalary'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'salaries'", 'to': u"orm['polidata.Politician']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['polisalary']