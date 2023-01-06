from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    TestModel.objects.create(name="name")
    all_names = TestModel.objects.all()
    return HttpResponse(all_names)