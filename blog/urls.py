from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.BlogHomeView.as_view(), name='blog')
]