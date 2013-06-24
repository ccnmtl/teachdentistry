# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DentalEducator.previous_dental_career'
        db.add_column('main_dentaleducator', 'previous_dental_career',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.CareerType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'DentalEducator.other_previous_dental_career'
        db.add_column('main_dentaleducator', 'other_previous_dental_career',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DentalEducator.other_current_dental_career'
        db.add_column('main_dentaleducator', 'other_current_dental_career',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field current_dental_career on 'DentalEducator'
        db.create_table('main_dentaleducator_current_dental_career', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dentaleducator', models.ForeignKey(orm['main.dentaleducator'], null=False)),
            ('careertype', models.ForeignKey(orm['main.careertype'], null=False))
        ))
        db.create_unique('main_dentaleducator_current_dental_career', ['dentaleducator_id', 'careertype_id'])


    def backwards(self, orm):
        # Deleting field 'DentalEducator.previous_dental_career'
        db.delete_column('main_dentaleducator', 'previous_dental_career_id')

        # Deleting field 'DentalEducator.other_previous_dental_career'
        db.delete_column('main_dentaleducator', 'other_previous_dental_career')

        # Deleting field 'DentalEducator.other_current_dental_career'
        db.delete_column('main_dentaleducator', 'other_current_dental_career')

        # Removing M2M table for field current_dental_career on 'DentalEducator'
        db.delete_table('main_dentaleducator_current_dental_career')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.careertype': {
            'Meta': {'object_name': 'CareerType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.clinicalfield': {
            'Meta': {'object_name': 'ClinicalField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.degree': {
            'Meta': {'object_name': 'Degree'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.dentaleducator': {
            'Meta': {'object_name': 'DentalEducator'},
            'academic_career': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dentaleducator_academic_career'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['main.CareerType']"}),
            'academic_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'bio_summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'career_stage': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'clinical_field': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.ClinicalField']", 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'contact_permission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current_dental_career': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dentaleducator_current_career'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['main.CareerType']"}),
            'degree': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Degree']", 'null': 'True', 'blank': 'True'}),
            'dental_career': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dentaleducator_dental_career'", 'null': 'True', 'to': "orm['main.CareerType']"}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'headshot': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Institution']"}),
            'institution_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_academic_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_current_dental_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_degree': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_dental_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_motivation': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_previous_dental_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'paid_time_commitment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.TimeCommitment']"}),
            'previous_dental_career': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.CareerType']", 'null': 'True', 'blank': 'True'}),
            'primary_motivation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Motivation']", 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'release_consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teaching_reason': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'teaching_responsibility': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.TeachingResponsibility']", 'symmetrical': 'False'}),
            'trainees_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'video': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'video_poster': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'volunteer_time_commitment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unpaid_time_commitment'", 'to': "orm['main.TimeCommitment']"}),
            'years_teaching': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        'main.institution': {
            'Meta': {'ordering': "['name']", 'object_name': 'Institution'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'main.motivation': {
            'Meta': {'object_name': 'Motivation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.teachingresponsibility': {
            'Meta': {'object_name': 'TeachingResponsibility'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.timecommitment': {
            'Meta': {'object_name': 'TimeCommitment'},
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_location': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_user'", 'to': "orm['auth.User']"})
        },
        'main.uservisited': {
            'Meta': {'object_name': 'UserVisited'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagetree.Section']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.UserProfile']"}),
            'visited_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'pagetree.hierarchy': {
            'Meta': {'object_name': 'Hierarchy'},
            'base_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'pagetree.section': {
            'Meta': {'object_name': 'Section'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'hierarchy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagetree.Hierarchy']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']