from django.test import TestCase
from django.urls import reverse, resolve

from .models import Faculty
from .views import FacultyListView


class FacultyTestModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_faculty = Faculty.objects.create(
            name="Facultad de Ingeniería", address="Calle 123",
            service_social_adviser="Adviser 1", professional_practices_adviser="Adviser 2"
        )

    def test_name(self):
        self.assertEqual(self.test_faculty.name, "Facultad de Ingeniería")

    def test_address(self):
        self.assertEqual(self.test_faculty.address, "Calle 123")

    def test_service_social_adviser(self):
        self.assertEqual(self.test_faculty.service_social_adviser, "Adviser 1")

    def test_professional_practices_adviser(self):
        self.assertEqual(self.test_faculty.professional_practices_adviser, "Adviser 2")

    def test_get_by_id(self):
        self.assertEqual(Faculty.objects.get(id=1), self.test_faculty)

    def tearDown(self):
        self.test_faculty.delete()


class FacultyTestURLCase(TestCase):

    def test_list_url(self):
        url = reverse('faculty-list')
        self.assertEqual(resolve(url).view_name, 'faculty-list')

    def test_create_url(self):
        url = reverse('faculty-create')
        self.assertEqual(resolve(url).view_name, 'faculty-create')