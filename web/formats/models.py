from formats.utils import PDFGeneratorAPI
from django.db import models
from core.utils import ProgramChoices


# Create your models here.
class Document(models.Model, PDFGeneratorAPI):
    name = models.CharField(max_length=50)
    api_identifier = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=500, null=True)
    mode = models.CharField(max_length=3, choices=ProgramChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "documents"
        verbose_name = 'Formato'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.api_identifier = self.create_template(self.name, self.mode)
        return super().save(args, kwargs)
