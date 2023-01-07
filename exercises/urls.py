from django.urls import path

from . import views

urlpatterns = [
    path('', views.superheroes, name='superheroes'),
    path('animals', views.animals, name='animals'),
    path('cars', views.cars, name='cars'),
    path('templates', views.templates, name='templates'),
    path('summary', views.summary, name='summary'),
    
    path('submit_form', views.submit_form, name='submit_form'),
    path('team_edward', views.team_edward, name='team_edward'),
    path('team_jacob', views.team_jacob, name='team_jacob'),
]