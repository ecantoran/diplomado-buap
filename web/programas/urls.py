from django.urls import path

from programas.views import CompanyListView, ProgramListView, \
    ProgramCreateView, CompanyCreateView, CompanyDetailView, ProgramDetailView, ProgramEnrollView

urlpatterns = [
    path('programs/create/', ProgramCreateView.as_view(), name='program-create'),
    path('programs/', ProgramListView.as_view(), name='program-list'),
    path('programs/<int:pk>/', ProgramDetailView.as_view(), name='program_detail'),
    path('programs/<int:pk>/enroll/', ProgramEnrollView.as_view(), name='program_enroll'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company_detail')
]
