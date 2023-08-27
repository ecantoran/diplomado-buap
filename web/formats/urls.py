from django.urls import path

from formats.views import DocumentView, DocumentListView, DocumentCreateView, DocumentDetailView, DocumentUpdateView, \
    DocumentGeneratePDF

urlpatterns = [
    # path('documents/', DocumentView.as_view(), name='documents-demo')
    path('documents/', DocumentListView.as_view(), name='documents-list'),
    path('documents/create/', DocumentCreateView.as_view(), name='documents-create'),
    path(r"documents/<int:pk>/", DocumentDetailView.as_view(), name='documents-detail'),
    path(r"documents/<int:pk>/update/", DocumentUpdateView.as_view(), name='documents-update'),
    path(r"documents/<int:pk>/download/", DocumentGeneratePDF.as_view(), name='documents-delete'),
]
