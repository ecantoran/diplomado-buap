from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import ProgramChoices, SectorChoices


class Program(models.Model):

    name = models.CharField(max_length=150)
    folio = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    kind = models.CharField(choices=ProgramChoices.choices, max_length=3)
    area = models.CharField(max_length=50)
    company = models.ForeignKey(
        "programas.Company",
        on_delete=models.CASCADE
    )
    faculty = models.ForeignKey(
        "facultades.Faculty",
        on_delete=models.CASCADE,
        related_name="programs"
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "program"

    def __str__(self):
        return self.name + " - " + self.folio


class Company(models.Model):

    name = models.CharField(_("Name"), max_length=200)
    street = models.CharField(_("Street"), max_length=120)
    colony = models.CharField(_("Colony"), max_length=20)
    cp = models.CharField(_("Postal Code"), max_length=7)
    state = models.CharField(_("State"), max_length=50)
    municipality = models.CharField(_("Municipality"), max_length=50)
    sector = models.CharField(_("Sector"), choices=SectorChoices.choices, max_length=10)
    phone = models.CharField(max_length=18)
    director = models.CharField(_("Director's full name"), max_length=200)
    area_manager = models.CharField(_("Area manager full name"), max_length=200)
    officer = models.CharField(_("Officer full name"), max_length=200)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.name
