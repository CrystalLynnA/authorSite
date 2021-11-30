from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
import datetime
from . models import *

def index(request):
    context = {
        "year" : datetime.datetime.today().year}
    return render(request, 'index.html', context)
   
def bio(request):
    context = {
        "year" : datetime.datetime.today().year}
    return render(request, 'bio.html', context)

def hardestYear(request):
    context = {
        "year" : datetime.datetime.today().year}
    return render(request,'hardestYear.html', context)

def anthologies(request):
    context = {
        "year" : datetime.datetime.today().year}
    return render(request,'anthologies.html', context)

def contact(request):
    context = {
        "year" : datetime.datetime.today().year}
    return render(request, 'contact.html', context)
    