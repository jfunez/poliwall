# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActionCategory'
        db.create_table(u'polisessions_actioncategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'polisessions', ['ActionCategory'])

        # Adding field 'Action.category'
        db.add_column(u'polisessions_action', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polisessions.ActionCategory'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ActionCategory'
        db.delete_table(u'polisessions_actioncategory')

        # Deleting field 'Action.category'
        db.delete_column(u'polisessions_action', 'category_id')


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
        u'polisessions.action': {
            'Meta': {'ordering': "['session']", 'object_name': 'Action'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polisessions.ActionCategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'legislative_actions'", 'to': u"orm['polidata.Legislative']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions'", 'to': u"orm['polidata.Politician']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polisessions.Session']"}),
            'source_url': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'polisessions.actioncategory': {
            'Meta': {'object_name': 'ActionCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'polisessions.session': {
            'Meta': {'ordering': "['date', 'ordinal']", 'object_name': 'Session'},
            'assists_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'session_houses'", 'to': u"orm['polidata.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'session_legislatives'", 'to': u"orm['polidata.Legislative']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'president': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'presidents'", 'null': 'True', 'to': u"orm['polidata.Politician']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['polisessions']