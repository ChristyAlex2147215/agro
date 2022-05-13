# Create your views here.
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Customer(request):
    customer=customer.objects.all()
    custDict={'customer':customer}
    return render(request,'customer.html',custDict)