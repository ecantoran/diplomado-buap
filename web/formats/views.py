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
        print(context)
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
        print(context)
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
            "nombre": "Demo",
            "apellido": "User",
            "matricula": "12345"
        }