from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    service_social_adviser = models.CharField(max_length=250)
    professional_practices_adviser = models.CharField(max_length=250)

    class Meta:
        db_table = "faculty"


class Career(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=20)
    faculty = models.ForeignKey('facultades.Faculty', on_delete=models.CASCADE)

    class Meta:
        db_table = "career"


class Student(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDERS = (
        (MALE, _('male')),
        (FEMALE, _('female'))
    )
    name = models.CharField(max_length=50)
    first_surname = models.CharField(_("Father's surname"), max_length=40)
    second_surname = models.CharField(_("Mother's surname"), max_length=40)
    tuition = models.CharField(max_length=9, unique=True)
    address = models.CharField(_("Direction address"), max_length=250)
    career = models.ForeignKey('facultades.Career', on_delete=models.PROTECT)
    gender = models.CharField(max_length=6, choices=GENDERS)
    birth_day = models.DateField()

