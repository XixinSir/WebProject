from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")
