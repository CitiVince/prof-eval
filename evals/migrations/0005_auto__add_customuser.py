# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table('evals_customuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('evals', ['CustomUser'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table('evals_customuser')


    models = {
        'evals.comment': {
            'Meta': {'object_name': 'Comment'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evals.Professor']", 'null': 'True', 'blank': 'True'}),
            'rating_clarity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_easiness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_interesting': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_niceness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_overall': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'evals.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'evals.professor': {
            'Meta': {'object_name': 'Professor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pre_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['evals.University']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'evals.university': {
            'Meta': {'object_name': 'University'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['evals']