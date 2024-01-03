from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Index.html")

def About(request):
    return render(request, "AboutUs.html")

def Cannabis(request):
    return render(request, "Cannabis.html")

def contactus(request):
    return render(request, "contactus.html")

