# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Professor.rating_niceness'
        db.delete_column('evals_professor', 'rating_niceness')

        # Deleting field 'Professor.rating_overall'
        db.delete_column('evals_professor', 'rating_overall')

        # Deleting field 'Professor.rating_easiness'
        db.delete_column('evals_professor', 'rating_easiness')

        # Deleting field 'Professor.rating_interesting'
        db.delete_column('evals_professor', 'rating_interesting')

        # Deleting field 'Professor.rating_clarity'
        db.delete_column('evals_professor', 'rating_clarity')


    def backwards(self, orm):
        # Adding field 'Professor.rating_niceness'
        db.add_column('evals_professor', 'rating_niceness',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Professor.rating_overall'
        db.add_column('evals_professor', 'rating_overall',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Professor.rating_easiness'
        db.add_column('evals_professor', 'rating_easiness',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Professor.rating_interesting'
        db.add_column('evals_professor', 'rating_interesting',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'Professor.rating_clarity'
        db.add_column('evals_professor', 'rating_clarity',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=1, blank=True),
                      keep_default=False)


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