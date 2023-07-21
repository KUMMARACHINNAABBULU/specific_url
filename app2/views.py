from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>this is django class</h1>')

def second(request):
    return HttpResponse('<h1>poraaa</h1>')