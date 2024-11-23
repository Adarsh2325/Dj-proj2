from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def peter(request):
    return HttpResponse('I am Spiderman')
