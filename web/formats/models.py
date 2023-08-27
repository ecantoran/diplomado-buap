from formats.utils import PDFGeneratorAPI
from django.db import models



# Create your models here.
class Document(models.Model, PDFGeneratorAPI):
    name = models.CharField(max_length=50)
    api_identifier = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    content = models.TextField()
    mode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "documents"
        verbose_name = 'Formato'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.api_identifier = self.create_template(self.name, self.mode)
        return super().save(args, kwargs)
