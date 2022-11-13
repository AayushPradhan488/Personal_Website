from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('html5up-forty/index.html')
    return HttpResponse(template.render())

def error(request):
    template = loader.get_template('html5up-forty/errorpage.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('html5up-forty/landing.html')
    return HttpResponse(template.render())

def generic(request):
    template = loader.get_template('html5up-forty/generic.html')
    return HttpResponse(template.render())

def elements(request):
    template = loader.get_template('html5up-forty/elements.html')
    return HttpResponse(template.render())
