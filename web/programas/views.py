from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

from programas.models import Program, Company


class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'facultades/faculty_create.html'
    success_url = '/programs/'


class ProgramListView(ListView):
    model = Program
    template_name = 'programas/program_list.html'
    # context_object_name = 'faculties'
    paginate_by = 10


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programas/program_detail.html'


class CompanyCreateView(CreateView):
    model = Company
    fields = '__all__'
    template_name = 'programas/company_create.html'
    success_url = '/companies/'


class CompanyListView(ListView):
    model = Company
    templates = 'programas/company_list.html'
    paginate_by = 10


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'facultades/company_detail.html'
