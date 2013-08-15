from django.contrib.auth.models import User
from teachdentistry.main.models import UserProfile, DentalEducator
from teachdentistry.main.models import Institution, PrimaryTraineesType
from teachdentistry.main.models import TimeCommitment
import factory


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: "user%03d" % n)
    is_staff = True


class UserProfileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = UserProfile
    user = factory.SubFactory(UserFactory)
    year_of_graduation = 2000


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
