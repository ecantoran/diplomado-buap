from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, CreateView

from facultades.models import Faculty


class FacultyCreateView(CreateView):
    model = Faculty
    fields = '__all__'
    template_name = 'facultades/faculty_create.html'
    success_url = '/faculties/'


class FacultyListView(ListView):
    model = Faculty
    template_name = 'facultades/faculty_list.html'
    # context_object_name = 'faculties'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
