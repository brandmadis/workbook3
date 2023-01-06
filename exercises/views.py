# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero, Animal, Car
from django.urls import reverse



# Create your views here.
def superheroes(request):
    
    # code below!
    superheroes = Superhero.objects.filter(name="wolverine")
    
    context = { 'superheroes': superheroes }
    return render(request, 'exercises/superhero.html', context)       


def animals(request):
    animals = None
    
    # code below!
    # animals = Animal.objects.all()
    
    context = { 'animals': animals }
    return render(request, 'exercises/animal.html', context)       

def cars(request):
    cars = None
    
    # code below!
    cars = Car.objects.all()
    
    context = { 'cars': cars }
    return render(request, 'exercises/car.html', context)       


def templates(request):
    
    superheroes = Superhero.objects.all()
    
    context = { 'superheroes': superheroes }
    return render(request, 'exercises/template.html', context)       

def summary(request):
    
    context = {  }
    return render(request, 'exercises/summary.html', context)       
    

def submit_form(request):
    context = { }
    return render(request, "exercises/submit_form.html", context)
    
def team_edward(request):
    return HttpResponse(request.POST['message'] + " is a fervent supporter of team edward")
    
def team_jacob(request):
    return HttpResponse(request.POST['message'] + " is a member of team jacob. ROAR!!")
    
    
