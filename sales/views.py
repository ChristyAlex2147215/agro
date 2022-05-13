from django.shortcuts import render
from sales.models import sales
# Create your views here.


def Sales(request):
    sale=sales.objects.all()
    salesDict={'sale':sale}
    return render(request,'sales.html',salesDict)