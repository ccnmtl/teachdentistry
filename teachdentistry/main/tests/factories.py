from django.contrib.auth.models import User
from teachdentistry.main.models import UserProfile, DentalEducator
from teachdentistry.main.models import Institution, PrimaryTraineesType
from teachdentistry.main.models import TimeCommitment
from pagetree.models import Hierarchy, Section
import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: "user%03d" % n)
    is_staff = True


class UserProfileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UserProfile
    user = factory.SubFactory(UserFactory)
    gender = 'M'
    year_of_graduation = 2000
    primary_discipline = 'S1'
    primary_other_dental_discipline = ''
    primary_other_discipline = ''
    work_description = 'coding'
    state = 'NY'
    dental_school = 'Other'
    postal_code = '10027'
    plan_to_teach = 'A3'
    qualified_to_teach = 'A3'
    opportunities_to_teach = 'A3'
    possible_to_teach = 'A3'
    ethnicity = 'E2'
    race = 'R6'
    age = 'G3'
    highest_degree = 'D3'
    consented = True


class InstitutionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Institution
    name = factory.Sequence(lambda n: "institution%03d" % n)
    latitude = 0.
    longitude = 0.


class PrimaryTraineesTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PrimaryTraineesType
    name = factory.Sequence(lambda n: "pt%03d" % n)


class TimeCommitmentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TimeCommitment
    duration = "one year"


class DentalEducatorFactory(factory.DjangoModelFactory):
    FACTORY_FOR = DentalEducator
    first_name = factory.Sequence(lambda n: "fname%03d" % n)
    last_name = factory.Sequence(lambda n: "lname%03d" % n)
    institution = factory.SubFactory(InstitutionFactory)
    primary_trainees_type = factory.SubFactory(PrimaryTraineesTypeFactory)
    paid_time_commitment = factory.SubFactory(TimeCommitmentFactory)
    volunteer_time_commitment = factory.SubFactory(TimeCommitmentFactory)


class HierarchyFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Hierarchy
    name = "main"
    base_url = ""


class RootSectionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Section
    hierarchy = factory.SubFactory(HierarchyFactory)
    label = "Root"
    slug = ""
