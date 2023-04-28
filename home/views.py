from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


from datetime import datetime
# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'