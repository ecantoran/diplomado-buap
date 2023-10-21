from django.db import models
from django.utils.translation import gettext_lazy as _


class ProgramChoices(models.TextChoices):
    SOCIAL_SERVICE = "SS", _("Social Service")
    PROFESSIONAL_PRACTICES = "PP", _("Professional Practice")


class SectorChoices(models.TextChoices):
    PUBLIC = "public", _("Public")
    PRIVATE = "private", _("Private")
