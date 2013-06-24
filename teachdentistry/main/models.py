from django.db import models
from django.contrib.auth.models import User
from pagetree.models import Section


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

RACE_CHOICES = (
    ('R1', 'Black/African American'),
    ('R2', 'White'),
    ('R3', 'Native Hawaiian or Other Pacific Islander'),
    ('R4', 'Asian'),
    ('R5', 'American Indian/Alaska Native'),
    ('R6', 'Other')
)

ETHNICITY_CHOICES = (
    ('E1', 'Hispanic or Latino'),
    ('E2', 'Non-Hispanic or Non-Latino')
)

CAREER_STAGE_CHOICES = (
    ('E', 'Early career'),
    ('M', 'Mid career'),
    ('L', 'Late career')
)


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="application_user")
    last_location = models.CharField(max_length=255, default="/")

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
    other_trainees_type = models.CharField(max_length=256, null=True, blank=True)
    teaching_responsibility = models.ManyToManyField(TeachingResponsibility)
    paid_time_commitment = models.ForeignKey(TimeCommitment)
    volunteer_time_commitment = models.ForeignKey(
        TimeCommitment,
        related_name="unpaid_time_commitment")
    career_stage = models.CharField(max_length=1, choices=CAREER_STAGE_CHOICES)
    years_teaching = models.CharField(max_length=256, null=True, blank=True)
    previous_dental_career = models.ForeignKey(CareerType, null=True, blank=True)
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
