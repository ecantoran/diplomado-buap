from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from formats.models import Document


# Create your views here.
class DocumentView(TemplateView):
    template_name = 'formats/index.html'


class DocumentListView(ListView):
    model = Document
    template_name = "formats/list_formats.html"


class DocumentCreateView(CreateView):
    model = Document
    fields = ['name', 'description', 'mode']
    template_name = 'formats/create_format.html'
    success_url = "/documents/"

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'formats/detail_format.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DocumentUpdateView(UpdateView):
    model = Document
    fields = ['name', 'description', 'mode']
    template_name = 'formats/update_format.html'
    success_url = "/documents/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["api_url"] = instance.create_ulr_view()
        return context

class DocumentGeneratePDF(View):

    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Document.objects.get(pk=pk)
            data = self.get_user_data("user")

            return instance.generate_document(data)

        except Document.DoesNotExist:
            raise Http404

    def get_user_data(self, user):
        return {
            'email': "alumno@alumno.com",
            'name': "Ramon",
            'first_surname': "Garcia",
            'second_surname': "Garcia",
            'matricula': "201116415",
            'address': "Av. Independencia 123",
            'postal_code': "72000",
            'phone': "123456789",
            'birthdate': "1992-01-01",
            'social_service_name': "Programa especial de servicios",
            'social_service_folio': "SS2012842",
            'professional_practices_name': "Programa de especial para profesionales",
            'professional_practices_folio': "PP9092432",
            'faculty_name': "Facultad de Ingeniería en Todologia",
            "service_social_adviser": "Juan Perez Perez",
            "professional_practices_adviser": "Ricardo Rodriguez Torres",
        }