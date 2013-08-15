from django.test import TestCase
from django.test.client import Client
from .factories import UserProfileFactory, DentalEducatorFactory
from .factories import HierarchyFactory


class BasicViewTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_root(self):
        response = self.c.get("/")
        self.assertEquals(response.status_code, 302)  # redirect to login

    def test_smoketest(self):
        response = self.c.get("/smoketest/")
        self.assertEquals(response.status_code, 200)
        # this test is just to check that the smoketests are able to
        # run without an error. They are not expected to have to pass


class LoggedInViewTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.up = UserProfileFactory()
        self.user = self.up.user
        self.user.set_password("test")
        self.user.save()
        self.c.login(username=self.user.username, password="test")

    def test_index(self):
        response = self.c.get("/")
        self.assertEquals(response.status_code, 200)

    def test_de_profile(self):
        root = HierarchyFactory().get_root()
        root.add_child_section_from_dict(dict(label="map", slug="map"))
        de = DentalEducatorFactory()
        response = self.c.get("/profile/%d/" % de.id)
        self.assertEqual(response.status_code, 200)

    def test_page(self):
        root = HierarchyFactory().get_root()
        root.add_child_section_from_dict(dict(label="map", slug="map"))
        response = self.c.get("/map/")
        self.assertEqual(response.status_code, 200)

    def test_page_post(self):
        root = HierarchyFactory().get_root()
        root.add_child_section_from_dict(dict(label="map", slug="map"))
        response = self.c.post("/map/")
        self.assertEqual(response.status_code, 302)

    def test_edit_page(self):
        root = HierarchyFactory().get_root()
        root.add_child_section_from_dict(dict(label="map", slug="map"))
        response = self.c.get("/edit/map/")
        self.assertEqual(response.status_code, 200)

    def test_instructor_page(self):
        root = HierarchyFactory().get_root()
        root.add_child_section_from_dict(dict(label="map", slug="map"))
        response = self.c.get("/instructor/map/")
        self.assertEqual(response.status_code, 403)

        self.user.is_superuser = True
        self.user.save()
        response = self.c.get("/instructor/map/")
        self.assertEqual(response.status_code, 200)
