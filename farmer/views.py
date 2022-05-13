# Create your views here.
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def basicelem(request):
    return render(request,'basic_elements.html')

def basictable(request):
    return render(request,'basic-table.html')

def charts(request):
    return render(request,'chartjs.html')