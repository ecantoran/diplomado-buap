from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from core.forms import CompanyRegistryForm
from programas.models import Company


# Create your views here.
class Index(TemplateView):
    template_name = "core/index.html"


class CompanyRegistryView(CreateView):
    model = Company
    form_class = CompanyRegistryForm
    template_name = 'core/company_registry.html'
    success_url = '/'
