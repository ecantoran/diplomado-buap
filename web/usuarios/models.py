from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

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

    company = models.ForeignKey(
        'programas.Company',
        on_delete=models.SET_NULL,
        null=True
    )

    manager = CustomUserManager()

    def __str__(self):
        return self.email