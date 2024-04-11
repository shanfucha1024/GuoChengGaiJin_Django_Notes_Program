from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,'home.html')

# home_page = None

# Create your views here.
