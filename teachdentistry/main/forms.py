from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from localflavor.us.us_states import US_STATES
from registration.forms import RegistrationForm

from teachdentistry.main.choices import GENDER_CHOICES, DISCIPLINE_CHOICES, \
    DENTAL_SCHOOL_CHOICES, ETHNICITY_CHOICES, RACE_CHOICES_EX, AGE_CHOICES, \
    DEGREE_CHOICES, WORK_CHOICES, AGREEMENT_CHOICES, AGREEMENT_CHOICES_EX


class UserProfileForm(RegistrationForm):
    consented = forms.BooleanField(
        label="""I have read the consent agreement and agree to the terms
        and conditions.""")

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
        I plan to teach dentistry (full or part time) in the future""")

    qualified_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES,
        label="""How much would you say you agree with this statement:
        I feel confident that I  have the skills required to enter
        dental academics""")

    opportunities_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES,
        label="""How much would you say you agree with this statement:
        I know where to find opportunities in dental academics""")

    possible_to_teach = forms.ChoiceField(
        choices=AGREEMENT_CHOICES_EX,
        label="""How much would you say you agree with this statement:
        The benefits of entering dental academics outweigh the challenges""")

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
