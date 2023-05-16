from django.urls import path

from facultades.views import FacultyListView, FacultyCreateView

urlpatterns = [
    path('faculties/', FacultyListView.as_view(), name='faculty-list'),
    path(
        'faculties/create/',
        FacultyCreateView.as_view(),
        name='faculty-create')
]
