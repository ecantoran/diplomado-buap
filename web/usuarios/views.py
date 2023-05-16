from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from .forms import NameForm

# Create your views here.

class LoginView(TemplateView):
    template_name = "users/login.html"


class FormView(View):
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
