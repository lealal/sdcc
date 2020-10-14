from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.listings, name='projects'),
    path('blog/', views.news, name='blog'),
    path('contact/', views.contact, name='contact')
]