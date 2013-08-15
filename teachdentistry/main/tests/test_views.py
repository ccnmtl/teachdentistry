from django.test import TestCase
from django.test.client import Client


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


