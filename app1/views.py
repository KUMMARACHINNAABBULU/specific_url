from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h2>this is....</h2>')

def second(request):
    return HttpResponse('<h2><marquee>AVASARAMA</marquee></h2>')