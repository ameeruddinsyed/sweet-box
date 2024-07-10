from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    
    s='<h1>i am software developer</h1>'
    
    return HttpResponse(s)
