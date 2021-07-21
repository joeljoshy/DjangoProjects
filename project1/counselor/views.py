from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  follow_ups(request):

    return HttpResponse('<h1>Follow Ups</h1>')

def  admissions(request):

    return HttpResponse('<h1>Admissions</h1>')
