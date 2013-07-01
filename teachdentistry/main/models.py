from django import forms
from django.contrib.auth.models import User
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from pagetree.models import Section
from registration.forms import RegistrationForm
from teachdentistry.main.choices import GENDER_CHOICES, \
    DISCIPLINE_CHOICES, AGREEMENT_CHOICES, AGREEMENT_CHOICES_EX, \
    ETHNICITY_CHOICES, RACE_CHOICES_EX, AGE_CHOICES, DEGREE_CHOICES, \
    WORK_CHOICES, RACE_CHOICES, CAREER_STAGE_CHOICES, DENTAL_SCHOOL_CHOICES


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
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)

    gender = forms.ChoiceField(
        initial="-----", choices=GENDER_CHOICES, label='Your gender')

    primary_discipline = forms.ChoiceField(
        choices=DISCIPLINE_CHOICES,
        label="Your primary professional discipline")

    primary_other_dental_discipline = forms.CharField(
        max_length=1024, required=False,
        label='If "Dentistry, Other", please specify')

    primary_other_discipline = forms.CharField(
        max_length=1024, required=False,
        label='If "Other", please specify')

    dental_school = forms.ChoiceField(
        choices=DENTAL_SCHOOL_CHOICES,
        label="Where did you attend dental school?")

    year_of_graduation = forms.IntegerField(
        min_value=1900, max_value=3000,
        label="What year did you graduate?")

    postal_code = forms.CharField(
        max_length=10,
        label="Zip code of your current residence")

    ethnicity = forms.ChoiceField(choices=ETHNICITY_CHOICES)
    race = forms.ChoiceField(choices=RACE_CHOICES_EX)
    age = forms.ChoiceField(choices=AGE_CHOICES)
    highest_degree = forms.ChoiceField(
        choices=DEGREE_CHOICES,
        label="Highest degree earned")

    state = forms.MultipleChoiceField(
        choices=US_STATES,
        label=" Please tell us what state you work in (select all that apply)")

    work_description = forms.MultipleChoiceField(
        choices=WORK_CHOICES,
        label="Please describe your work (select all that apply)",
        widget=CheckboxSelectMultiple())

    plan_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES,
        label="""How much would you say you agree with this statement:
        I plan to teach dentistry (full or part time) in the future:""")

    qualified_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES,
        label="""How much would you say you agree with this statement:
        I feel confident that I  have the skills required to enter
        dental academics:""")

    opportunities_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES,
        label="""How much would you say you agree with this statement:
        I know where to find opportunities in dental academics:""")

    possible_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES_EX,
        label="""How much would you say you agree with this statement:
        The benefits of entering dental academics outweigh the challenges:""")

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
