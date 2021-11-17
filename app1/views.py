from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from . models import *

def index(request):
    return render(request, 'index.html')
   
def bio(request):
    return render(request, 'bio.html')

def hardestYear(request):
    return render(request,'hardestYear.html')

def anthologies(request):
    return render(request,'anthologies.html')

def contact(request):
    return render(request, 'contact.html')