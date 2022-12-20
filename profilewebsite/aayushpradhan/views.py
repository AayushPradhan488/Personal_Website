from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('html5up-forty/index.html')
    return HttpResponse(template.render())

def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'html5up-forty/errorpage2.html')

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

def RubiksCubeSolver(request):
    template = loader.get_template('html5up-forty/RubiksCubeSolver.html')
    return HttpResponse(template.render())

def MySociety(request):
    template = loader.get_template('html5up-forty/MySociety.html')
    return HttpResponse(template.render())

def BirthdayManager(request):
    template = loader.get_template('html5up-forty/BirthdayManager.html')
    return HttpResponse(template.render())

def InvoManager(request):
    template = loader.get_template('html5up-forty/InvoManager.html')
    return HttpResponse(template.render())

def Simulation(request):
    template = loader.get_template('html5up-forty/Simulation.html')
    return HttpResponse(template.render())

def SudokuSolver(request):
    template = loader.get_template('html5up-forty/SudokuSolver.html')
    return HttpResponse(template.render())
