from django.test import TestCase

from teachdentistry.main.models import TeachDentistryReport, Motivation, \
    TeachingResponsibility
from teachdentistry.main.tests.factories import HierarchyFactory, UserFactory

from .factories import UserProfileFactory, DentalEducatorFactory


class UserProfileTest(TestCase):
    def test_unicode(self):
        up = UserProfileFactory()
        self.assertEqual(str(up), up.user.username)

    def test_displayname(self):
        up = UserProfileFactory()
        self.assertEqual(up.display_name(), up.user.username)


class DentalEducatorTest(TestCase):
    def test_unicode(self):
        de = DentalEducatorFactory()
        self.assertEqual(str(de), "%s %s" % (de.first_name, de.last_name))

    def test_display_name(self):
        de = DentalEducatorFactory()
        self.assertEqual(de.educator_display_name(),
                         "%s %s" % (de.first_name, de.last_name))
        de.display_name = "this one instead"
        self.assertEqual(de.educator_display_name(),
                         "this one instead")


class ModelTests(TestCase):

    def test_unicode(self):
        x = Motivation.objects.create(name='motivation')
        self.assertEquals(x.__unicode__(), 'motivation')

        x = TeachingResponsibility.objects.create(name='responsibility')
        self.assertEquals(x.__unicode__(), 'responsibility')


class TeachDentistryReportTest(TestCase):

    def setUp(self):
        self.hierarchy = HierarchyFactory()

        self.report = TeachDentistryReport()

        self.profile = UserProfileFactory()

        UserFactory(is_superuser=True)

    def test_get_users(self):
        users = self.report.users()
        self.assertEquals(len(users), 1)
        self.assertEquals(users[0], self.profile.user)

    def test_metadata(self):
        rows = self.report.metadata([self.hierarchy])

        header = ['hierarchy', 'itemIdentifier', 'exercise type',
                  'itemType', 'itemText', 'answerIdentifier',
                  'answerText']
        self.assertEquals(rows.next(), header)

        self.assertEquals(rows.next(), "")

        # username
        self.assertEquals(rows.next()[1], 'userid')
        self.assertEquals(rows.next()[1], 'gender')
        self.assertEquals(rows.next()[1], 'primary_discipline')
        self.assertEquals(rows.next()[1], 'primary_other_discipline')
        self.assertEquals(rows.next()[1], 'primary_other_dental_discipline')
        self.assertEquals(rows.next()[1], 'work_description')
        self.assertEquals(rows.next()[1], 'state')
        self.assertEquals(rows.next()[1], 'year_of_graduation')
        self.assertEquals(rows.next()[1], 'dental_school')
        self.assertEquals(rows.next()[1], 'postal_code')
        self.assertEquals(rows.next()[1], 'plan_to_teach')
        self.assertEquals(rows.next()[1], 'qualified_to_teach')
        self.assertEquals(rows.next()[1], 'opportunities_to_teach')
        self.assertEquals(rows.next()[1], 'possible_to_teach')
        self.assertEquals(rows.next()[1], 'ethnicity')
        self.assertEquals(rows.next()[1], 'race')
        self.assertEquals(rows.next()[1], 'age')
        self.assertEquals(rows.next()[1], 'highest_degree')
        self.assertEquals(rows.next()[1], 'consented')

    def test_values(self):
        rows = self.report.values([self.hierarchy])
        rows.next()  # header

        row = rows.next()
        self.assertEquals(row[0], self.profile.user.pk)
        self.assertEquals(row[1], 'M')
        self.assertEquals(row[2], 'S1')
        self.assertEquals(row[3], '')
        self.assertEquals(row[4], '')
        self.assertEquals(row[5], 'coding')
        self.assertEquals(row[6], 'NY')
        self.assertEquals(row[7], 2000)

        self.assertEquals(row[8], 'Other')
        self.assertEquals(row[9], '10027')
        self.assertEquals(row[10], 'A3')
        self.assertEquals(row[11], 'A3')
        self.assertEquals(row[12], 'A3')
        self.assertEquals(row[13], 'A3')
        self.assertEquals(row[14], 'E2')
        self.assertEquals(row[15], 'R6')
        self.assertEquals(row[16], 'G3')
        self.assertEquals(row[17], 'D3')
        self.assertEquals(row[18], True)
