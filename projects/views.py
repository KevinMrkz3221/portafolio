from django.shortcuts import render
from django.views.generic import ListView, TemplateView


from .models import Projects
# Create your views here.


class ProjectsView(ListView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'projects/projects_list.html'
    