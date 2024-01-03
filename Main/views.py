from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def mainnDash(request):
     return render(request, 'Dashboard.html')

     
def map1(request):
     return render(request,'map.html')


def map2(request):
     return render(request,'map2.html')


def map3(request):
     return render(request,'map3.html')


    