from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/projects', views.projects, name='projects'),
    path('/join', views.join, name='join'),
    path('/contact', views.contact, name='contact'),
]