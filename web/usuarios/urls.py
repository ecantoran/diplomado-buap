from django.contrib import admin
from django.urls import path

from .views import LoginView, FormView, LogoutView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('form/', FormView.as_view()),
    path('profile/', UserProfileView.as_view()),
]
