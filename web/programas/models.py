from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Program(models.Model):
    class KindChoices(models.IntegerChoices):
        SS = 0, _("Social Service")
        PP = 1, _("Professional Practice")

    name = models.CharField(max_length=150)
    folio = models.CharField(max_length=30)
    kind = models.IntegerField(choices=KindChoices.choices)
    area = models.CharField(max_length=50)
    company = models.ForeignKey(
        "programas.Company",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "program"


class Company(models.Model):
    class SectorChoices(models.IntegerChoices):
        PUBLIC = 0, _("Public")
        PRIVATE = 1, _("Private")

    name = models.CharField(_("Name"), max_length=200)
    street = models.CharField(_("Street"), max_length=120)
    colony = models.CharField(_("Colony"), max_length=20)
    cp = models.CharField(_("Postal Code"), max_length=7)
    state = models.CharField(_("State"), max_length=50)
    municipality = models.CharField(_("Municipality"), max_length=50)
    sector = models.IntegerField(_("Sector"), choices=SectorChoices.choices)
    phone = models.CharField(max_length=18)
    director = models.CharField(_("Director's full name"), max_length=200)
    area_manager = models.CharField(_("Area manager full name"), max_length=200)
    officer = models.CharField(_("Officer full name"), max_length=200)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.name
