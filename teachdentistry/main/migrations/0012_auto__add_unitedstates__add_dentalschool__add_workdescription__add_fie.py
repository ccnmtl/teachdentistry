# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from teachdentistry.main.models import DentalSchool

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UnitedStates'
        db.create_table('main_unitedstates', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('main', ['UnitedStates'])

        # Adding model 'DentalSchool'
        db.create_table('main_dentalschool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('main', ['DentalSchool'])
        ds = DentalSchool(id=0, name='Placeholder')
        ds.save()

        # Adding model 'WorkDescription'
        db.create_table('main_workdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('main', ['WorkDescription'])

        # Adding field 'UserProfile.gender'
        db.add_column('main_userprofile', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='F', max_length=1),
                      keep_default=False)

        # Adding field 'UserProfile.primary_discipline'
        db.add_column('main_userprofile', 'primary_discipline',
                      self.gf('django.db.models.fields.CharField')(default='S1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.primary_other_dental_discipline'
        db.add_column('main_userprofile', 'primary_other_dental_discipline',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.primary_other_discipline'
        db.add_column('main_userprofile', 'primary_other_discipline',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.year_of_graduation'
        db.add_column('main_userprofile', 'year_of_graduation',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=2015),
                      keep_default=False)

        # Adding field 'UserProfile.dental_school'
        db.add_column('main_userprofile', 'dental_school',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['main.DentalSchool']),
                      keep_default=False)

        # Adding field 'UserProfile.postal_code'
        db.add_column('main_userprofile', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(default=10022, max_length=10),
                      keep_default=False)

        # Adding field 'UserProfile.plan_to_teach'
        db.add_column('main_userprofile', 'plan_to_teach',
                      self.gf('django.db.models.fields.CharField')(default='A1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.qualified_to_teach'
        db.add_column('main_userprofile', 'qualified_to_teach',
                      self.gf('django.db.models.fields.CharField')(default='A1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.opportunities_to_teach'
        db.add_column('main_userprofile', 'opportunities_to_teach',
                      self.gf('django.db.models.fields.CharField')(default='A1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.possible_to_teach'
        db.add_column('main_userprofile', 'possible_to_teach',
                      self.gf('django.db.models.fields.CharField')(default='A1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.ethnicity'
        db.add_column('main_userprofile', 'ethnicity',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.race'
        db.add_column('main_userprofile', 'race',
                      self.gf('django.db.models.fields.CharField')(default='R1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.age'
        db.add_column('main_userprofile', 'age',
                      self.gf('django.db.models.fields.CharField')(default='G1', max_length=2),
                      keep_default=False)

        # Adding field 'UserProfile.highest_degree'
        db.add_column('main_userprofile', 'highest_degree',
                      self.gf('django.db.models.fields.CharField')(default='D1', max_length=2),
                      keep_default=False)

        # Adding M2M table for field work_description on 'UserProfile'
        db.create_table('main_userprofile_work_description', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('workdescription', models.ForeignKey(orm['main.workdescription'], null=False))
        ))
        db.create_unique('main_userprofile_work_description', ['userprofile_id', 'workdescription_id'])

        # Adding M2M table for field state on 'UserProfile'
        db.create_table('main_userprofile_state', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['main.userprofile'], null=False)),
            ('unitedstates', models.ForeignKey(orm['main.unitedstates'], null=False))
        ))
        db.create_unique('main_userprofile_state', ['userprofile_id', 'unitedstates_id'])


    def backwards(self, orm):
        # Deleting model 'UnitedStates'
        db.delete_table('main_unitedstates')

        # Deleting model 'DentalSchool'
        db.delete_table('main_dentalschool')

        # Deleting model 'WorkDescription'
        db.delete_table('main_workdescription')

        # Deleting field 'UserProfile.gender'
        db.delete_column('main_userprofile', 'gender')

        # Deleting field 'UserProfile.primary_discipline'
        db.delete_column('main_userprofile', 'primary_discipline')

        # Deleting field 'UserProfile.primary_other_dental_discipline'
        db.delete_column('main_userprofile', 'primary_other_dental_discipline')

        # Deleting field 'UserProfile.primary_other_discipline'
        db.delete_column('main_userprofile', 'primary_other_discipline')

        # Deleting field 'UserProfile.year_of_graduation'
        db.delete_column('main_userprofile', 'year_of_graduation')

        # Deleting field 'UserProfile.dental_school'
        db.delete_column('main_userprofile', 'dental_school_id')

        # Deleting field 'UserProfile.postal_code'
        db.delete_column('main_userprofile', 'postal_code')

        # Deleting field 'UserProfile.plan_to_teach'
        db.delete_column('main_userprofile', 'plan_to_teach')

        # Deleting field 'UserProfile.qualified_to_teach'
        db.delete_column('main_userprofile', 'qualified_to_teach')

        # Deleting field 'UserProfile.opportunities_to_teach'
        db.delete_column('main_userprofile', 'opportunities_to_teach')

        # Deleting field 'UserProfile.possible_to_teach'
        db.delete_column('main_userprofile', 'possible_to_teach')

        # Deleting field 'UserProfile.ethnicity'
        db.delete_column('main_userprofile', 'ethnicity')

        # Deleting field 'UserProfile.race'
        db.delete_column('main_userprofile', 'race')

        # Deleting field 'UserProfile.age'
        db.delete_column('main_userprofile', 'age')

        # Deleting field 'UserProfile.highest_degree'
        db.delete_column('main_userprofile', 'highest_degree')

        # Removing M2M table for field work_description on 'UserProfile'
        db.delete_table('main_userprofile_work_description')

        # Removing M2M table for field state on 'UserProfile'
        db.delete_table('main_userprofile_state')


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
            'academic_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'bio_summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'career_stage': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'clinical_field': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.ClinicalField']", 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'contact_permission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current_dental_career': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dentaleducator_current_career'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['main.CareerType']"}),
            'degree': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Degree']", 'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'headshot': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Institution']"}),
            'institution_state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_current_dental_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_degree': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_motivation': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_previous_dental_career': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'other_trainees_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'paid_time_commitment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.TimeCommitment']"}),
            'previous_dental_career': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.CareerType']", 'null': 'True', 'blank': 'True'}),
            'primary_motivation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main.Motivation']", 'null': 'True', 'blank': 'True'}),
            'primary_trainees_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.PrimaryTraineesType']"}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'release_consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teaching_reason': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'teaching_responsibility': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.TeachingResponsibility']", 'symmetrical': 'False'}),
            'video': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'video_poster': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'volunteer_time_commitment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unpaid_time_commitment'", 'to': "orm['main.TimeCommitment']"}),
            'years_teaching': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'main.dentalschool': {
            'Meta': {'object_name': 'DentalSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
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
        'main.primarytraineestype': {
            'Meta': {'object_name': 'PrimaryTraineesType'},
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
        'main.unitedstates': {
            'Meta': {'object_name': 'UnitedStates'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dental_school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.DentalSchool']"}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'highest_degree': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_location': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '255'}),
            'opportunities_to_teach': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'plan_to_teach': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'possible_to_teach': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'primary_discipline': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'primary_other_dental_discipline': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'primary_other_discipline': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'qualified_to_teach': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.UnitedStates']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_user'", 'to': "orm['auth.User']"}),
            'work_description': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.WorkDescription']", 'symmetrical': 'False'}),
            'year_of_graduation': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'main.uservisited': {
            'Meta': {'object_name': 'UserVisited'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagetree.Section']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.UserProfile']"}),
            'visited_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'main.workdescription': {
            'Meta': {'object_name': 'WorkDescription'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
