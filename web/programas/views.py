from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from core.utils import ProgramChoices
from programas.models import Program, Company


class ProgramCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Program
    fields = '__all__'
    template_name = 'programas/program_create.html'
    success_url = '/programs/'
    permission_required = ["programas.add_program"]

    def get_form_class(self):
        if self.request.user.is_superuser:
            self.fields = '__all__'
        else:
            self.fields = ['name', 'folio', 'description', 'kind', 'area', 'faculty']
        return super().get_form_class()

    def form_valid(self, form):
        if not  self.request.user.is_superuser:
            form.instance.company = self.request.user.company
        return super().form_valid(form)


class ProgramListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Program
    template_name = 'programas/program_list.html'
    # context_object_name = 'faculties'
    paginate_by = 10
    permission_required = ["programas.view_program"]

    def get_queryset(self):
        if self.request.user.company:
            return Program.objects.filter(company=self.request.user.company)
        else:
            return Program.objects.all()

class ProgramDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Program
    template_name = 'programas/program_detail.html'
    permission_required = ["programas.view_program"]


class ProgramEnrollView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Program
    permission_required = ["programas.view_program"]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user
        if getattr(user, 'student', None) is None:
            raise PermissionDenied
        else:
            if self.object.kind == ProgramChoices.PROFESSIONAL_PRACTICES:
                user.student.professional_practices = self.object
                user.student.save()
            else:
                user.student.social_service = self.object
                user.student.save()
        return redirect('profile')


class CompanyCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
    template_name = 'programas/company_create.html'
    success_url = '/companies/'
    permission_required = ["programas.add_company"]


class CompanyListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Company
    templates = 'programas/company_list.html'
    paginate_by = 10
    permission_required = ["programas.view_company"]


class CompanyDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'facultades/company_detail.html'
    permission_required = ["programas.view_company"]
