from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from formats.models import Document


# Create your views here.
class DocumentView(PermissionRequiredMixin, TemplateView):
    template_name = 'formats/index.html'
    permission_required = ["formats.view_document"]


class DocumentListView(PermissionRequiredMixin, ListView):
    model = Document
    template_name = "formats/list_formats.html"
    permission_required = ["formats.view_document"]


class DocumentCreateView(PermissionRequiredMixin, CreateView):
    model = Document
    fields = ['name', 'description', 'mode']
    template_name = 'formats/create_format.html'
    success_url = "/documents/"
    permission_required = ["formats.add_document"]

class DocumentDetailView(PermissionRequiredMixin, DetailView):
    model = Document
    template_name = 'formats/detail_format.html'
    permission_required = ["formats.view_document"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DocumentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Document
    fields = ['name', 'description', 'mode']
    template_name = 'formats/update_format.html'
    success_url = "/documents/"
    permission_required = ["formats.change_document"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["api_url"] = instance.create_ulr_view()
        return context

class DocumentGeneratePDF(PermissionRequiredMixin, View):
    permission_required = ["formats.view_document"]

    def get(self, request, pk, *args, **kwargs):
        if not request.user.student:
            raise PermissionDenied()
        try:
            instance = Document.objects.get(pk=pk)
            data = self.get_user_data(request.user)

            return instance.generate_document(data)

        except Document.DoesNotExist:
            raise Http404

    def get_user_data(self, user):
        return user.get_data_to_dict()