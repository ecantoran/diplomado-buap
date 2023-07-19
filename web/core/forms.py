from django.forms import ModelForm

from programas.models import Company


class CompanyRegistryForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['is_active']