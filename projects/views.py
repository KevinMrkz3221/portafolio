from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Projects
# Create your views here.


class ProjectsView(ListView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'projects/projects_list.html'

class ProjectsDetailView(DetailView):
    model = Projects
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'
    