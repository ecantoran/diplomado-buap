from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from facultades.models import Faculty


class FacultyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Faculty
    fields = '__all__'
    template_name = 'facultades/faculty_create.html'
    success_url = '/faculties/'
    permission_required = ["facultades.add_faculty"]


class FacultyListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Faculty
    template_name = 'facultades/faculty_list.html'
    # context_object_name = 'faculties'
    paginate_by = 100
    permission_required = ["programas.view_faculty"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
