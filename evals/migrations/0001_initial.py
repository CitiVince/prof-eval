# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Professor'
        db.create_table('evals_professor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pre_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evals.University'], null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rating_overall', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_clarity', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_interesting', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_easiness', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_niceness', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('evals', ['Professor'])

        # Adding model 'University'
        db.create_table('evals_university', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('evals', ['University'])

        # Adding model 'Comment'
        db.create_table('evals_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rating_overall', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_clarity', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_interesting', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_easiness', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('rating_niceness', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('evals', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Professor'
        db.delete_table('evals_professor')

        # Deleting model 'University'
        db.delete_table('evals_university')

        # Deleting model 'Comment'
        db.delete_table('evals_comment')


    models = {
        'evals.comment': {
            'Meta': {'object_name': 'Comment'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating_clarity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_easiness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_interesting': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_niceness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_overall': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'evals.professor': {
            'Meta': {'object_name': 'Professor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pre_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating_clarity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_easiness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_interesting': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_niceness': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'rating_overall': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
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