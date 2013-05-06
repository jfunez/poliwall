# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'polisessions_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legislative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sessions_legislatives', to=orm['polidata.Legislative'])),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(related_name='session_houses', to=orm['polidata.House'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ordinal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('president', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='presidents', null=True, to=orm['polidata.Politician'])),
            ('source_url', self.gf('django.db.models.fields.TextField')()),
            ('assists_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'polisessions', ['Session'])

        # Adding model 'Action'
        db.create_table(u'polisessions_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legislative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='legislative_actions', to=orm['polidata.Legislative'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polisessions.Session'])),
            ('source_url', self.gf('django.db.models.fields.TextField')()),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actions', to=orm['polidata.Politician'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'polisessions', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'polisessions_session')

        # Deleting model 'Action'
        db.delete_table(u'polisessions_action')


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
        u'polidata.politician': {
            'Meta': {'object_name': 'Politician'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'politician_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1', 'db_index': 'True'}),
            'twitter_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'polisessions.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'legislative_actions'", 'to': u"orm['polidata.Legislative']"}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actions'", 'to': u"orm['polidata.Politician']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polisessions.Session']"}),
            'source_url': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'polisessions.session': {
            'Meta': {'object_name': 'Session'},
            'assists_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'session_houses'", 'to': u"orm['polidata.House']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legislative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessions_legislatives'", 'to': u"orm['polidata.Legislative']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'president': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'presidents'", 'null': 'True', 'to': u"orm['polidata.Politician']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['polisessions']