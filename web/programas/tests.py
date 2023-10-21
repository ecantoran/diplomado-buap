from django.test import TestCase
from django.urls import reverse, resolve

from facultades.models import Faculty
from .models import Program, Company
from core.utils import ProgramChoices
# Create your tests here.


class CompanyTestModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_company = Company.objects.create(
            name="Empresa 1", street="Calle 123", colony="Colonia 1", cp="12345",
            state="Estado 1", municipality="Municipio 1", sector="Sector 1",
            phone="1234567890", director="Director 1", area_manager="Area manager 1",
            officer="Officer 1", is_active=True
        )

    def test_name(self):
        self.assertEqual(self.test_company.name, "Empresa 1")

    def test_street(self):
        self.assertEqual(self.test_company.street, "Calle 123")

    def test_colony(self):
        self.assertEqual(self.test_company.colony, "Colonia 1")

    def test_cp(self):
        self.assertEqual(self.test_company.cp, "12345")

    def test_state(self):
        self.assertEqual(self.test_company.state, "Estado 1")

    def test_municipality(self):
        self.assertEqual(self.test_company.municipality, "Municipio 1")

    def test_sector(self):
        self.assertEqual(self.test_company.sector, "Sector 1")

    def test_phone(self):
        self.assertEqual(self.test_company.phone, "1234567890")

    def test_director(self):
        self.assertEqual(self.test_company.director, "Director 1")

    def test_area_manager(self):
        self.assertEqual(self.test_company.area_manager, "Area manager 1")

    def test_officer(self):
        self.assertEqual(self.test_company.officer, "Officer 1")

    def test_is_active(self):
        self.assertEqual(self.test_company.is_active, True)

    def tearDown(self):
        self.test_company.delete()


class CompanyTestURLCase(TestCase):

    def test_list_url(self):
        url = reverse('company-list')
        self.assertEqual(resolve(url).view_name, 'company-list')

    def test_create_url(self):
        url = reverse('company-create')
        self.assertEqual(resolve(url).view_name, 'company-create')

    def test_detail_url(self):
        url = reverse('company-detail', args=[1])
        self.assertEqual(resolve(url).view_name, 'company-detail')


class ProgramTestModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_faculty = Faculty.objects.create(
            name="Facultad 1", address="Calle 123", service_social_adviser="Adviser 1",
        )
        company = Company.objects.create(
            name="Empresa 1", street="Calle 123", colony="Colonia 1", cp="12345",
            state="Estado 1", municipality="Municipio 1", sector="Sector 1",
            phone="1234567890", director="Director 1", area_manager="Area manager 1",
            officer="Officer 1", is_active=True
        )

        cls.test_program = Program.objects.create(
            name="Programa 1", folio="12345", description="Descripción 1",
            kind=ProgramChoices.SOCIAL_SERVICE, area="Area 1", company=company, faculty=test_faculty
        )
        cls.test_faculty = test_faculty
        cls.test_company = company

    def test_name(self):
        self.assertEqual(self.test_program.name, "Programa 1")

    def test_folio(self):
        self.assertEqual(self.test_program.folio, "12345")

    def test_description(self):
        self.assertEqual(self.test_program.description, "Descripción 1")

    def test_kind(self):
        self.assertEqual(self.test_program.kind, ProgramChoices.SOCIAL_SERVICE)

    def test_area(self):
        self.assertEqual(self.test_program.area, "Area 1")

    def tearDown(self):
        self.test_program.delete()


class ProgramTestURLCase(TestCase):

    def test_list_url(self):
        url = reverse('program-list')
        self.assertEqual(resolve(url).view_name, 'program-list')

    def test_create_url(self):
        url = reverse('program-create')
        self.assertEqual(resolve(url).view_name, 'program-create')

    def test_detail_url(self):
        url = reverse('program-detail', args=[1])
        self.assertEqual(resolve(url).view_name, 'program-detail')

    def test_enroll_url(self):
        url = reverse('program-enroll', args=[1])
        self.assertEqual(resolve(url).view_name, 'program-enroll')