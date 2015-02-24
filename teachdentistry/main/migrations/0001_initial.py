# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pagetree', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClinicalField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DentalEducator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('display_name', models.CharField(max_length=256, null=True, blank=True)),
                ('bio_summary', models.TextField(default=b'', null=True, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'-----', b'-----'), (b'M', b'Male'), (b'F', b'Female')])),
                ('contact_email', models.CharField(max_length=256, null=True, blank=True)),
                ('contact_permission', models.BooleanField(default=False)),
                ('release_consent', models.BooleanField(default=False)),
                ('race', models.CharField(blank=True, max_length=2, null=True, choices=[(b'R1', b'Black/African American'), (b'R2', b'White'), (b'R3', b'Native Hawaiian or Other Pacific Islander'), (b'R4', b'Asian'), (b'R5', b'American Indian/Alaska Native'), (b'R6', b'Other')])),
                ('ethnicity', models.CharField(blank=True, max_length=2, null=True, choices=[(b'-----', b'-----'), (b'E1', b'Hispanic or Latino'), (b'E2', b'Non-Hispanic or Non-Latino')])),
                ('headshot', models.FileField(null=True, upload_to=b'headshots/%Y/%m/%d/', blank=True)),
                ('academic_title', models.CharField(max_length=256, null=True, blank=True)),
                ('other_degree', models.CharField(max_length=256, null=True, blank=True)),
                ('institution_state', models.CharField(max_length=2, null=True, blank=True)),
                ('other_trainees_type', models.CharField(max_length=256, null=True, blank=True)),
                ('career_stage', models.CharField(max_length=1, choices=[(b'E', b'Early career'), (b'M', b'Mid career'), (b'L', b'Late career')])),
                ('years_teaching', models.CharField(max_length=256, null=True, blank=True)),
                ('other_previous_dental_career', models.CharField(max_length=256, null=True, blank=True)),
                ('other_current_dental_career', models.CharField(max_length=256, null=True, blank=True)),
                ('other_motivation', models.CharField(max_length=256, null=True, blank=True)),
                ('teaching_reason', models.TextField(default=b'', null=True, blank=True)),
                ('video', models.TextField(default=b'', null=True, blank=True)),
                ('video_poster', models.FileField(null=True, upload_to=b'video/%Y/%m/%d/', blank=True)),
                ('clinical_field', models.ManyToManyField(to='main.ClinicalField', null=True, blank=True)),
                ('current_dental_career', models.ManyToManyField(related_name='dentaleducator_current_career', null=True, to='main.CareerType', blank=True)),
                ('degree', models.ManyToManyField(to='main.Degree', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DentalSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=10)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrimaryTraineesType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeachingResponsibility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeCommitment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitedStates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_location', models.CharField(default=b'/', max_length=255)),
                ('gender', models.CharField(max_length=1, choices=[(b'-----', b'-----'), (b'M', b'Male'), (b'F', b'Female')])),
                ('primary_discipline', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'S1', b'Dentistry, general'), (b'S2', b'Dentistry, pediatric'), (b'S3', b'Dentistry, public health'), (b'S4', b'Dentistry, Other'), (b'S5', b'Other')])),
                ('primary_other_dental_discipline', models.CharField(max_length=1024, null=True, blank=True)),
                ('primary_other_discipline', models.CharField(max_length=1024, null=True, blank=True)),
                ('work_description', models.TextField()),
                ('state', models.TextField()),
                ('year_of_graduation', models.PositiveIntegerField()),
                ('dental_school', models.CharField(max_length=1024, choices=[(b'-----', b'-----'), (b'A.T. Still University Arizona School of Dentistry and Oral Health', b'A.T. Still University Arizona School of Dentistry and Oral Health'), (b'Baylor College of Dentistry Component of Texas A &amp; M Health Sci Ctr', b'Baylor College of Dentistry Component of Texas A &amp; M\n     Health Sci Ctr'), (b'Boston University Goldman School of Dental Medicine', b'Boston University Goldman School of Dental Medicine'), (b'Case Western Reserve Univ. School of Dental Medicine', b'Case Western Reserve Univ. School of Dental Medicine'), (b'Columbia University College of Dental Medicine', b'Columbia University College of Dental Medicine'), (b'Creighton University School of Dentistry', b'Creighton University School of Dentistry'), (b'East Carolina University School of Dental Medicine', b'East Carolina University School of Dental Medicine'), (b'Georgia Health Sciences University School of Dentistry', b'Georgia Health Sciences University School of Dentistry'), (b'Harvard University School of Dental Medicine', b'Harvard University School of Dental Medicine'), (b'Herman Ostrow School of Dentistry of USC', b'Herman Ostrow School of Dentistry of USC'), (b'Howard University College of Dentistry', b'Howard University College of Dentistry'), (b'Indiana University School of Dentistry', b'Indiana University School of Dentistry'), (b'LECOM College of Dental Medicine', b'LECOM College of Dental Medicine'), (b'Loma Linda University School of Dentistry', b'Loma Linda University School of Dentistry'), (b'Louisiana State University School of Dentistry', b'Louisiana State University School of Dentistry'), (b'Marquette University School of Dentistry', b'Marquette University School of Dentistry'), (b'Medical University of South Carolina James B.\n        Edwards College of Dental Medicine', b'Medical University of South Carolina James B.\n         Edwards College of Dental Medicine'), (b'Meharry Medical College School of Dentistry', b'Meharry Medical College School of Dentistry'), (b'Midwestern University College of Dental Medicine - Arizona', b'Midwestern University College of Dental Medicine- Arizona'), (b'Midwestern University College of Dental Medicine- Illinois', b'Midwestern University College of Dental Medicine - Illinois'), (b'New York University College of Dentistry', b'New York University College of Dentistry'), (b'Nova Southeastern University College of Dental Medicine', b'Nova Southeastern University College of Dental Medicine'), (b'Ohio State University College of Dentistry', b'Ohio State University College of Dentistry'), (b'Oregon Health and Science University School of Dentistry', b'Oregon Health and Science University School of Dentistry'), (b'Southern Illinois University School of Dental Medicine', b'Southern Illinois University School of Dental Medicine'), (b'State University of New York at Buffalo School of Dental Medicine', b'State University of New York at Buffalo School of Dental Medicine'), (b'State University of New York at Stony Brook School of Dental Medicine', b'State University of New York at Stony Brook School of Dental Medicine'), (b'Temple University The Maurice H. Kornberg School of Dentistry', b'Temple University The Maurice H. Kornberg School of Dentistry'), (b'Tufts University School of Dental Medicine', b'Tufts University School of Dental Medicine'), (b'University of Alabama School of Dentistry at UAB', b'University of Alabama School of Dentistry at UAB'), (b'University of California at Los Angeles School of Dentistry', b'University of California at Los Angeles School of Dentistry'), (b'University of California at San Francisco School of Dentistry', b'University of California at San Francisco School of Dentistry'), (b'University of Colorado Denver', b'University of Colorado Denver'), (b'University of Connecticut School of Dental Medicine', b'University of Connecticut School of Dental Medicine'), (b'University of Detroit Mercy School of Dentistry', b'University of Detroit Mercy School of Dentistry'), (b'University of Florida College of Dentistry', b'University of Florida College of Dentistry'), (b'University of Illinois at Chicago College of Dentistry', b'University of Illinois at Chicago College of Dentistry'), (b'University of Iowa College of Dentistry', b'University of Iowa College of Dentistry'), (b'University of Kentucky College of Dentistry', b'University of Kentucky College of Dentistry'), (b'University of Louisville School of Dentistry', b'University of Louisville School of Dentistry'), (b'University of Maryland Baltimore College of Dental Surgery', b'University of Maryland Baltimore College of Dental Surgery'), (b'University of Medicine &amp; Dentistry of\n    New Jersey New Jersey Dental School', b'University of Medicine &amp; Dentistry of\n        New Jersey New Jersey Dental School'), (b'University of Michigan School of Dentistry', b'University of Michigan School of Dentistry'), (b'University of Minnesota School of Dentistry', b'University of Minnesota School of Dentistry'), (b'University of Mississippi School of Dentistry', b'University of Mississippi School of Dentistry'), (b'University of Missouri - Kansas City School of Dentistry', b'University of Missouri-Kansas City School of Dentistry'), (b'University of Nebraska Medical Center College of Dentistry', b'University of Nebraska Medical Center College of Dentistry'), (b'University of Nevada Las Vegas School of Dental Medicine', b'University of Nevada Las Vegas School of Dental Medicine'), (b'University of North Carolina School of Dentistry', b'University of North Carolina School of Dentistry'), (b'University of Oklahoma College of Dentistry', b'University of Oklahoma College of Dentistry'), (b'University of Pennsylvania School of Dental Medicine', b'University of Pennsylvania School of Dental Medicine'), (b'University of Pittsburgh School of Dental Medicine', b'University of Pittsburgh School of Dental Medicine'), (b'University of Puerto Rico School of Dental Medicine', b'University of Puerto Rico School of Dental Medicine'), (b'University of Tennessee College of Dentistry', b'University of Tennessee College of Dentistry'), (b'University of Texas Hlth Science Cnt-San Antonio Dental School', b'University of Texas Hlth Science Cnt - San Antonio Dental School'), (b'University of Texas School of Dentistry at Houston', b'University of Texas School of Dentistry at Houston'), (b'University of the Pacific Arthur A. Dugoni School of Dentistry', b'University of the Pacific Arthur A. Dugoni School of Dentistry'), (b'University of Washington-Health Sciences School of Dentistry', b'University of Washington-Health Sciences School of Dentistry'), (b'Virginia Commonwealth University School of Dentistry', b'Virginia Commonwealth University School of Dentistry'), (b'West Virginia University School of Dentistry', b'West Virginia University School of Dentistry'), (b'Western University of Health Sciences College of Dental Medicine', b'Western University of Health Sciences College of Dental Medicine'), (b'Other', b'Other')])),
                ('postal_code', models.CharField(max_length=10)),
                ('plan_to_teach', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'A1', b'Strongly agree'), (b'A2', b'Agree'), (b'A3', b'Neutral'), (b'A4', b'Disagree'), (b'A5', b'Strongly disagree')])),
                ('qualified_to_teach', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'A1', b'Strongly agree'), (b'A2', b'Agree'), (b'A3', b'Neutral'), (b'A4', b'Disagree'), (b'A5', b'Strongly disagree')])),
                ('opportunities_to_teach', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'A1', b'Strongly agree'), (b'A2', b'Agree'), (b'A3', b'Neutral'), (b'A4', b'Disagree'), (b'A5', b'Strongly disagree')])),
                ('possible_to_teach', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'A1', b'Strongly agree'), (b'A2', b'Agree'), (b'A3', b'Neutral'), (b'A4', b'Disagree'), (b'A5', b'Strongly disagree'), (b'A6', b"I don't know the benefits"), (b'A7', b"I don't know the challenges"), (b'A8', b"I don't know the benefits or the challenges")])),
                ('ethnicity', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'E1', b'Hispanic or Latino'), (b'E2', b'Non-Hispanic or Non-Latino')])),
                ('race', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'R1', b'American Indian or Alaska Native'), (b'R2', b'Chinese, Filipino, Japanese, Korean, Asian Indian, or Thai'), (b'R3', b'Other Asian'), (b'R4', b'Black or African American'), (b'R5', b'Native Hawaiian or other Pacific Islander'), (b'R6', b'White')])),
                ('age', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'G1', b'Under 20'), (b'G2', b'20-29'), (b'G3', b'30-39'), (b'G4', b'40-49'), (b'G5', b'50-59'), (b'G6', b'60-69'), (b'G7', b'70 or older')])),
                ('highest_degree', models.CharField(max_length=2, choices=[(b'-----', b'-----'), (b'D1', b'High School diploma/GED'), (b'D2', b'Associate Degree or Equivalent'), (b'D3', b"Bachelor's Degree or Equivalent"), (b'D4', b"Master's Degree"), (b'D5', b'DDS or DMD'), (b'D6', b'MD'), (b'D7', b'PhD'), (b'D8', b'Other Doctorate')])),
                ('consented', models.BooleanField(default=False)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserVisited',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visited_time', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(to='pagetree.Section')),
                ('user', models.ForeignKey(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='institution',
            field=models.ForeignKey(to='main.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='paid_time_commitment',
            field=models.ForeignKey(to='main.TimeCommitment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='previous_dental_career',
            field=models.ForeignKey(blank=True, to='main.CareerType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='primary_motivation',
            field=models.ManyToManyField(to='main.Motivation', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='primary_trainees_type',
            field=models.ForeignKey(to='main.PrimaryTraineesType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='teaching_responsibility',
            field=models.ManyToManyField(to='main.TeachingResponsibility'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dentaleducator',
            name='volunteer_time_commitment',
            field=models.ForeignKey(related_name='unpaid_time_commitment', to='main.TimeCommitment'),
            preserve_default=True,
        ),
    ]
