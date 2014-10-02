from django.test import TestCase
from django.test.client import Client, RequestFactory
from teachdentistry.main.models import UserProfile
from teachdentistry.main.views import update_user_profile
from .factories import UserFactory, UserProfileFactory, DentalEducatorFactory
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

    def test_update_user_profile(self):
        user = UserFactory()
        data = {
            'first_name': 'john',
            'last_name': 'doe',
            'gender': 'M',
            'primary_discipline': 'S1',
            'primary_other_dental_discipline': '',
            'primary_other_discipline': '',
            'work_description': 'coding',
            'state': 'NY',
            'year_of_graduation': 2014,
            'dental_school': 'Other',
            'postal_code': '10027',
            'plan_to_teach': 'A3',
            'qualified_to_teach': 'A3',
            'opportunities_to_teach': 'A3',
            'possible_to_teach': 'A3',
            'ethnicity': 'E2',
            'race': 'R6',
            'age': 'G3',
            'highest_degree': 'D3',
            'consented': True
        }
        request = RequestFactory().post('', data)
        update_user_profile(None, user, request)
        qs = UserProfile.objects.filter(user=user)
        self.assertEquals(qs.count(), 1)
        self.assertEquals(qs[0].user.first_name, 'john')
        self.assertEquals(qs[0].user.last_name, 'doe')
        self.assertEquals(qs[0].gender, 'M')
        self.assertEquals(qs[0].primary_discipline, 'S1')
        self.assertEquals(qs[0].primary_other_dental_discipline, '')
        self.assertEquals(qs[0].primary_other_discipline, '')
        self.assertEquals(qs[0].work_description, 'coding')
        self.assertEquals(qs[0].state, 'NY')
        self.assertEquals(qs[0].year_of_graduation, 2014)
        self.assertEquals(qs[0].dental_school, 'Other')
        self.assertEquals(qs[0].postal_code, '10027')
        self.assertEquals(qs[0].plan_to_teach, 'A3')
        self.assertEquals(qs[0].qualified_to_teach, 'A3')
        self.assertEquals(qs[0].opportunities_to_teach, 'A3')
        self.assertEquals(qs[0].possible_to_teach, 'A3')
        self.assertEquals(qs[0].ethnicity, 'E2')
        self.assertEquals(qs[0].race, 'R6')
        self.assertEquals(qs[0].age, 'G3')
        self.assertEquals(qs[0].highest_degree, 'D3')
        self.assertEquals(qs[0].consented, True)


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
