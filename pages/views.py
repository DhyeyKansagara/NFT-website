from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home_start(request):
    return render(request, 'hello.html')
