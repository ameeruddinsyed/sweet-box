from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    
    return HttpResponse('<h1>i am team coordinator of python developers')