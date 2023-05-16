from django.contrib import admin
from django.urls import path

from .views import LoginView, FormView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('form/', FormView.as_view())
]
