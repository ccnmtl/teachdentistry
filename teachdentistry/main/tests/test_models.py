from django.test import TestCase
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
