from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.


class BlogHomeView(TemplateView):
    template_name = 'blog/overview.html'