from django.urls import path

from core.views import Index, CompanyRegistryView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('company-registry', CompanyRegistryView.as_view(), name='company-registry')
]
