from django.contrib.auth.models import User
from pagetree.reports import PagetreeReport, StandaloneReportColumn
from localflavor.us.us_states import US_STATES
from django.db import models
from pagetree.models import Section
from teachdentistry.main.choices import GENDER_CHOICES, \
    DISCIPLINE_CHOICES, AGREEMENT_CHOICES, AGREEMENT_CHOICES_EX, \
    ETHNICITY_CHOICES, RACE_CHOICES_EX, AGE_CHOICES, DEGREE_CHOICES, \
    RACE_CHOICES, CAREER_STAGE_CHOICES, DENTAL_SCHOOL_CHOICES


class DentalSchool(models.Model):
    name = models.CharField(max_length=1024)


class UnitedStates(models.Model):
    name = models.CharField(max_length=2, choices=US_STATES)


class WorkDescription(models.Model):
    description = models.CharField(max_length=1024)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
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
    consented = models.BooleanField(default=False)

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
    contact_permission = models.BooleanField(default=False)
    release_consent = models.BooleanField(default=False)
    race = models.CharField(max_length=2, choices=RACE_CHOICES,
                            null=True, blank=True)
    ethnicity = models.CharField(max_length=2, choices=ETHNICITY_CHOICES,
                                 null=True, blank=True)
    headshot = models.FileField(
        upload_to="headshots/%Y/%m/%d/", null=True, blank=True)
    academic_title = models.CharField(max_length=256, null=True, blank=True)
    clinical_field = models.ManyToManyField(ClinicalField, blank=True)
    degree = models.ManyToManyField(Degree, blank=True)
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
        CareerType, blank=True, related_name="dentaleducator_current_career")
    other_current_dental_career = models.CharField(max_length=256,
                                                   null=True, blank=True)
    primary_motivation = models.ManyToManyField(Motivation, blank=True)
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


class TeachDentistryReport(PagetreeReport):

    def users(self):
        users = User.objects.filter(
            is_superuser=False)
        return users.order_by('id')

    def get_profile_value(self, user, attr_name):
        try:
            return getattr(user.profile, attr_name)
        except:
            return 'nothing'

    def standalone_columns(self):
        return [
            StandaloneReportColumn(
                "date_joined", 'profile', 'string',
                'Date joined', lambda x: x.date_joined),
            StandaloneReportColumn(
                "userid", 'profile', 'string',
                'Unique ID', lambda x: x.pk),
            StandaloneReportColumn(
                "gender", 'profile', 'char',
                GENDER_CHOICES, lambda x: self.get_profile_value(x, 'gender')),
            StandaloneReportColumn(
                "primary_discipline", 'profile', 'string',
                DISCIPLINE_CHOICES,
                lambda x: self.get_profile_value(x, 'primary_discipline')),
            StandaloneReportColumn(
                "primary_other_discipline", 'profile', 'string',
                'Primary other discipline',
                lambda x: self.get_profile_value(
                    x, 'primary_other_discipline')),
            StandaloneReportColumn(
                "primary_other_dental_discipline", 'profile', 'string',
                'Primary other dental discipline',
                lambda x: self.get_profile_value(
                    x, 'primary_other_dental_discipline')),
            StandaloneReportColumn(
                "work_description", 'profile', 'string',
                'Work description',
                lambda x: self.get_profile_value(x, 'work_description')),
            StandaloneReportColumn(
                "state", 'profile', 'string',
                'State',
                lambda x: self.get_profile_value(x, 'state')),
            StandaloneReportColumn(
                "year_of_graduation", 'profile', 'integer',
                'Year of graduation',
                lambda x: self.get_profile_value(x, 'year_of_graduation')),
            StandaloneReportColumn(
                "dental_school", 'profile', 'string',
                DENTAL_SCHOOL_CHOICES,
                lambda x: self.get_profile_value(x, 'dental_school')),
            StandaloneReportColumn(
                "postal_code", 'profile', 'string',
                'Postal code',
                lambda x: self.get_profile_value(x, 'postal_code')),
            StandaloneReportColumn(
                "plan_to_teach", 'profile', 'string',
                AGREEMENT_CHOICES,
                lambda x: self.get_profile_value(x, 'plan_to_teach')),
            StandaloneReportColumn(
                "qualified_to_teach", 'profile', 'string',
                AGREEMENT_CHOICES,
                lambda x: self.get_profile_value(x, 'qualified_to_teach')),
            StandaloneReportColumn(
                "opportunities_to_teach", 'profile', 'string',
                AGREEMENT_CHOICES,
                lambda x: self.get_profile_value(x, 'opportunities_to_teach')),
            StandaloneReportColumn(
                "possible_to_teach", 'profile', 'string',
                AGREEMENT_CHOICES_EX,
                lambda x: self.get_profile_value(x, 'possible_to_teach')),
            StandaloneReportColumn(
                "ethnicity", 'profile', 'string',
                ETHNICITY_CHOICES,
                lambda x: self.get_profile_value(x, 'ethnicity')),
            StandaloneReportColumn(
                "race", 'profile', 'string',
                RACE_CHOICES_EX,
                lambda x: self.get_profile_value(x, 'race')),
            StandaloneReportColumn(
                "age", 'profile', 'string',
                AGE_CHOICES,
                lambda x: self.get_profile_value(x, 'age')),
            StandaloneReportColumn(
                "highest_degree", 'profile', 'string',
                DEGREE_CHOICES,
                lambda x: self.get_profile_value(x, 'highest_degree')),
            StandaloneReportColumn(
                "consented", 'profile', 'boolean',
                'Consent given',
                lambda x: self.get_profile_value(x, 'consented'))]
