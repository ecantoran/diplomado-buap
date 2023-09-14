from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from facultades.models import Faculty
from usuarios.managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    STUDENT = 'student'
    COMPANY = 'company'
    TEACHER = 'teacher'

    ROL_CHOICES = (
        (ADMIN, _('Admin')),
        (STUDENT, _('Student')),
        (COMPANY, _('Company')),
        (TEACHER, _('Teacher')),
    )
    # SOCIAL_SERVICE = 'social service'
    # PROFESSIONAL_PRACTICES = 'professional practices'
    email = models.EmailField(unique=True)
    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    rol = models.CharField(max_length=7, choices=ROL_CHOICES)
    name = models.CharField(max_length=40)
    first_surname = models.CharField(max_length=40)
    second_surname = models.CharField(max_length=40)

    company = models.OneToOneField(
        'programas.Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    manager = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"

    def get_data_to_dict(self):
        social_service = getattr(self.student, "social_service", None)
        professional_practices = getattr(self.student, "professional_practices", None)
        service_company = getattr(social_service, "company", None)
        professional_company = getattr(professional_practices, "company", None)

        data = {
            'email': self.email,
            'name': self.name,
            'first_surname': self.first_surname,
            'second_surname': self.second_surname,
            'matricula': getattr(self.student, "tuition", ""),
            'address': getattr(self.student, "address", ""),
            'postal_code': getattr(self.student, "postal_code", ""),
            'phone': getattr(self.student, "phone", ""),
            'birthdate': str(getattr(self.student, "birthdate", "")),
            'social_service_name': getattr(social_service, "name", ""),
            'social_service_folio': getattr(social_service, "folio", ""),
            'social_service_description': getattr(social_service, "description", ""),
            'social_service_program_adviser': getattr(service_company, "officer", "-----"),
            'professional_practices_name': getattr(professional_practices, "name", ""),
            'faculty_name': getattr(self.student.faculty, "name", ""),
            "service_social_adviser": getattr(self.student.faculty, "service_social_adviser", ""),
            "professional_practices_adviser": getattr(self.student.faculty, "professional_practices_adviser", ""),
            'professional_practices_description': getattr(professional_practices, "description", ""),
            'professional_practices_program_adviser': getattr(professional_company, "officer", "----")
        }
        return data

class Student(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDERS = (
        (MALE, _('male')),
        (FEMALE, _('female'))
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student')
    tuition = models.CharField(max_length=12, unique=True, default='')
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDERS)
    social_service = models.ForeignKey(
        'programas.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='social_students'
    )
    professional_practices = models.ForeignKey(
        'programas.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='professional_students'
    )
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )
    class Meta:
        db_table = "student"

    def __str__(self):
        return self.tuition

