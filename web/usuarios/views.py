from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView

from diplomado import settings
from formats.models import Document
from .forms import NameForm, LoginForm
from .models import CustomUser


# Create your views here.


class LoginView(View):
    template_name = "users/login.html"
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/profile/")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        contex = {"form": form}
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("login")
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/profile/")
            else:
                print("invalid user")
                messages.error(request, "Invalid username or password.")
        else:
            print("Invalid form")
            messages.error(request, "Invalid username or password.")
        return render(
            request=request,
            template_name=self.template_name,
            context=contex
        )


class LogoutView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        logout(request)
        return redirect("/")


class FormView(LoginRequiredMixin, View):
    form_class = NameForm
    initial = {'key': 'value'}
    template_name = 'users/form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            context["result"] = form.cleaned_data
            print("Success")
        return render(request, self.template_name, context=context)


class UserProfileView(LoginRequiredMixin, View):
    model = CustomUser
    template_name = 'users/profile.html'
    def get(self, request, *args, **kwargs):
        documents = Document.objects.all()
        context = {
            'documents': documents
        }
        return render(request, self.template_name, context=context)
