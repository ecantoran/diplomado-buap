from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "faculty"


class Career(models.Model):
    name = models.CharField(max_length=120)
    abbreviation = models.CharField(max_length=20)
    faculty = models.ForeignKey('facultades.Faculty', on_delete=models.CASCADE)

    class Meta:
        db_table = "career"
