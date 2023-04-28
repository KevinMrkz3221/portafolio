from django.urls import path

from . import views
urlpatterns =[
    path('portfolio', views.ProjectsView.as_view(), name='portfolio.list')
]