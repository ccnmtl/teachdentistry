from django.contrib.auth.models import User
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models
from pagetree.models import Section
from registration.forms import RegistrationForm
from django import forms
from django.utils.translation import ugettext_lazy as _


AGE_CHOICES = (
    ('-----', '-----'),
    ('G1', 'Under 20'),
    ('G2', '20-29'),
    ('G3', '30-39'),
    ('G4', '40-49'),
    ('G5', '50-59'),
    ('G6', '60-69'),
    ('G7', '70 or older'),
)

AGREEMENT_CHOICES = (
    ('-----', '-----'),
    ('A1', 'Strongly agree'),
    ('A2', 'Agree'),
    ('A3', 'Neutral'),
    ('A4', 'Disagree'),
    ('A5', 'Strongly disagree')
)

AGREEMENT_CHOICES_EX = (
    ('-----', '-----'),
    ('A1', 'Strongly agree'),
    ('A2', 'Agree'),
    ('A3', 'Neutral'),
    ('A4', 'Disagree'),
    ('A5', 'Strongly disagree'),
    ('A6', "I don't know the benefits"),
    ('A7', "I don't know the challenges"),
    ('A8', "I don't know the benefits or the challenges")
)


CAREER_STAGE_CHOICES = (
    ('E', 'Early career'),
    ('M', 'Mid career'),
    ('L', 'Late career')
)

DEGREE_CHOICES = (
    ('-----', '-----'),
    ('D1', 'High School diploma/GED'),
    ('D2', 'Associate Degree or Equivalent'),
    ('D3', "Bachelor's Degree or Equivalent"),
    ('D4', "Master's Degree"),
    ('D5', 'DDS or DMD'),
    ('D6', 'MD'),
    ('D7', 'PhD'),
    ('D8', 'Other Doctorate'),
)

DENTAL_SCHOOL_CHOICES = (
    ('-----', '-----'),
    ('Institution', 'Institution Foo Bar'),
)

DISCIPLINE_CHOICES = (
    ('-----', '-----'),
    ('S1', 'Dentistry, general'),
    ('S2', 'Dentistry, pediatric'),
    ('S3', 'Dentistry, public health'),
    ('S4', 'Dentistry, Other'),
    ('S5', 'Other'),
)

ETHNICITY_CHOICES = (
    ('-----', '-----'),
    ('E1', 'Hispanic or Latino'),
    ('E2', 'Non-Hispanic or Non-Latino')
)

RACE_CHOICES = (
    ('R1', 'Black/African American'),
    ('R2', 'White'),
    ('R3', 'Native Hawaiian or Other Pacific Islander'),
    ('R4', 'Asian'),
    ('R5', 'American Indian/Alaska Native'),
    ('R6', 'Other')
)

RACE_CHOICES_EX = (
    ('-----', '-----'),
    ('R1', 'American Indian or Alaska Native'),
    ('R2', 'Chinese, Filipino, Japanese, Korean, Asian Indian, or Thai'),
    ('R3', 'Other Asian'),
    ('R4', 'Black or African American'),
    ('R5', 'Native Hawaiian or other Pacific Islander'),
    ('R6', 'White'),
)

GENDER_CHOICES = (
    ('-----', '-----'),
    ('M', 'Male'),
    ('F', 'Female')
)

WORK_CHOICES = (
    ('C1', 'Clinical practice, Full time private practice'),
    ('C2', 'Clinical practice, Part time private practice'),
    ('C3', 'Clinical practice, Full time clinical safety net practice'),
    ('C4', 'Clinical practice, Part time clinical safety net practice'),
    ('C5', """Non-clinical practice: Full time non-clinical work in academica
        (includes teaching and research, advocacy, and the public sector)"""),
    ('C6', """Non-clinical practice: Part time non-clinical work in academia
        (includes teaching and research, advocacy and
        the public health sector)"""),
    ('C7', """Non-clinical practice: Full time non-clinical work in
        the corporate sector"""),
    ('C8', """Non-clinical practice: part time non-clinical work in the
        corporate sector"""),
)


class DentalSchool(models.Model):
    name = models.CharField(max_length=1024)


class UnitedStates(models.Model):
    name = models.CharField(max_length=2, choices=US_STATES)


class WorkDescription(models.Model):
    description = models.CharField(max_length=1024)


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="application_user")
    last_location = models.CharField(max_length=255, default="/")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    primary_discipline = models.CharField(max_length=2,
        choices=DISCIPLINE_CHOICES)
    primary_other_dental_discipline = models.CharField(
        max_length=1024, null=True, blank=True)
    primary_other_discipline = models.CharField(
        max_length=1024, null=True, blank=True)
    work_description = models.TextField()
    state = models.TextField()
    year_of_graduation = models.PositiveIntegerField()
    dental_school = models.CharField(max_length=1024,
                                     choices=DENTAL_SCHOOL_CHOICES)
    postal_code = models.CharField(max_length=10)
    plan_to_teach = models.CharField(max_length=2,
        choices=AGREEMENT_CHOICES)
    qualified_to_teach = models.CharField(max_length=2,
        choices=AGREEMENT_CHOICES)
    opportunities_to_teach = models.CharField(max_length=2,
        choices=AGREEMENT_CHOICES)
    possible_to_teach = models.CharField(max_length=2,
        choices=AGREEMENT_CHOICES_EX)
    ethnicity = models.CharField(max_length=2, choices=ETHNICITY_CHOICES)
    race = models.CharField(max_length=2, choices=RACE_CHOICES_EX)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    highest_degree = models.CharField(max_length=2, choices=DEGREE_CHOICES)

    def __unicode__(self):
        return self.user.username

    def display_name(self):
        return self.user.username

    def save_visit(self, section):
        self.last_location = section.get_absolute_url()
        self.save()
        uv, created = UserVisited.objects.get_or_create(
            user=self, section=section)

    def save_visits(self, sections):
        for s in sections:
            self.save_visit(s)

    def has_visited(self, section):
        return UserVisited.objects.filter(
            user=self, section=section).count() > 0
        return True


class UserProfileForm(RegistrationForm):
    gender = forms.ChoiceField(initial="-----", choices=GENDER_CHOICES)

    primary_discipline = forms.ChoiceField(choices=DISCIPLINE_CHOICES)
    primary_other_dental_discipline = forms.CharField(max_length=1024,
                                                      required=False)
    primary_other_discipline = forms.CharField(max_length=1024,
                                               required=False)
    work_description = forms.MultipleChoiceField(choices=WORK_CHOICES)
    state = forms.MultipleChoiceField(choices=US_STATES)
    year_of_graduation = forms.IntegerField(min_value=1900, max_value=3000)
    dental_school = forms.ChoiceField(choices=DENTAL_SCHOOL_CHOICES)
    postal_code = forms.CharField(max_length=10)
    plan_to_teach = forms.ChoiceField(choices=AGREEMENT_CHOICES)
    qualified_to_teach = forms.ChoiceField(choices=AGREEMENT_CHOICES)
    opportunities_to_teach = forms.ChoiceField(choices=AGREEMENT_CHOICES)
    possible_to_teach = forms.ChoiceField(choices=AGREEMENT_CHOICES_EX)
    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES)
    race = forms.ChoiceField(choices=RACE_CHOICES_EX)
    age = forms.ChoiceField(choices=AGE_CHOICES)
    highest_degree = forms.ChoiceField(choices=DEGREE_CHOICES)

    def clean(self):
        return super(RegistrationForm, self).clean()

    def clean_choice(self, field_name):
        if self.cleaned_data[field_name] == u"-----":
            msg = u"This field is required."
            self._errors[field_name] = self.error_class([msg])
            del self.cleaned_data[field_name]
            return None
        else:
            return self.cleaned_data[field_name]

    def clean_gender(self):
        return self.clean_choice("gender")

    def clean_primary_discipline(self):
        return self.clean_choice('primary_discipline')

    def clean_dental_school(self):
        return self.clean_choice('dental_school')

    def clean_plan_to_teach(self):
        return self.clean_choice('plan_to_teach')

    def clean_qualified_to_teach(self):
        return self.clean_choice('qualified_to_teach')

    def clean_opportunities_to_teach(self):
        return self.clean_choice('opportunities_to_teach')

    def clean_possible_to_teach(self):
        return self.clean_choice('possible_to_teach')

    def clean_ethnicity(self):
        return self.clean_choice('ethnicity')

    def clean_race(self):
        return self.clean_choice('race')

    def clean_age(self):
        return self.clean_choice('age')

    def clean_highest_degree(self):
        return self.clean_choice('highest_degree')
    

class UserVisited(models.Model):
    user = models.ForeignKey(UserProfile)
    section = models.ForeignKey(Section)
    visited_time = models.DateTimeField(auto_now=True)


class CareerType(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class ClinicalField(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=1024)
    latitude = models.DecimalField(max_digits=18, decimal_places=10)
    longitude = models.DecimalField(max_digits=18, decimal_places=10)

    def __unicode__(self):
        return "%s (%.6f,%.6f)" % (self.name, self.latitude, self.longitude)

    class Meta:
        ordering = ['name']


class Motivation(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class PrimaryTraineesType(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class TeachingResponsibility(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class TimeCommitment(models.Model):
    duration = models.CharField(max_length=256)

    def __unicode__(self):
        return self.duration


class DentalEducator(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256, null=True, blank=True)
    bio_summary = models.TextField(default='', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_email = models.CharField(max_length=256, null=True, blank=True)
    contact_permission = models.BooleanField()
    release_consent = models.BooleanField()
    race = models.CharField(max_length=2, choices=RACE_CHOICES,
                            null=True, blank=True)
    ethnicity = models.CharField(max_length=2, choices=ETHNICITY_CHOICES,
                                 null=True, blank=True)
    headshot = models.FileField(
        upload_to="headshots/%Y/%m/%d/", null=True, blank=True)
    academic_title = models.CharField(max_length=256, null=True, blank=True)
    clinical_field = models.ManyToManyField(ClinicalField,
                                            null=True, blank=True)
    degree = models.ManyToManyField(Degree, null=True, blank=True)
    other_degree = models.CharField(max_length=256, null=True, blank=True)
    institution = models.ForeignKey(Institution)
    institution_state = models.CharField(max_length=2, null=True, blank=True)
    primary_trainees_type = models.ForeignKey(PrimaryTraineesType)
    other_trainees_type = models.CharField(max_length=256,
                                           null=True, blank=True)
    teaching_responsibility = models.ManyToManyField(TeachingResponsibility)
    paid_time_commitment = models.ForeignKey(TimeCommitment)
    volunteer_time_commitment = models.ForeignKey(
        TimeCommitment,
        related_name="unpaid_time_commitment")
    career_stage = models.CharField(max_length=1, choices=CAREER_STAGE_CHOICES)
    years_teaching = models.CharField(max_length=256, null=True, blank=True)
    previous_dental_career = models.ForeignKey(CareerType,
                                               null=True, blank=True)
    other_previous_dental_career = models.CharField(max_length=256,
                                                    null=True, blank=True)
    current_dental_career = models.ManyToManyField(
        CareerType, null=True, blank=True,
        related_name="dentaleducator_current_career")
    other_current_dental_career = models.CharField(max_length=256,
                                                   null=True, blank=True)
    primary_motivation = models.ManyToManyField(Motivation,
                                                null=True, blank=True)
    other_motivation = models.CharField(max_length=256, null=True, blank=True)
    teaching_reason = models.TextField(default='', null=True, blank=True)
    video = models.TextField(default='', null=True, blank=True)
    video_poster = models.FileField(
        upload_to="video/%Y/%m/%d/", null=True, blank=True)

    def educator_display_name(self):
        if self.display_name:
            return self.display_name
        else:
            return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.educator_display_name()
