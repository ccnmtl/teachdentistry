from django.test import TestCase
from django.test.client import Client
from django.contrib import auth
from .factories import UserProfileFactory
from .factories import HierarchyFactory
from teachdentistry.main.helpers import get_or_create_profile


class HelpersTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.up = UserProfileFactory()
        self.user = self.up.user
        self.user.set_password("test")
        self.user.save()
        self.root = HierarchyFactory().get_root()
        self.root.add_child_section_from_dict(dict(label="map", slug="map"))

    def test_get_create_profile(self):
        # Anonymous user
        self.assertIsNone(get_or_create_profile(auth.get_user(self.c),
                          self.root))
        # Logged in user with profile
        self.assertEquals(get_or_create_profile(self.user, self.root), self.up)
