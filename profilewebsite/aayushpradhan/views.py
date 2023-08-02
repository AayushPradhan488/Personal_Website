from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('dev/index.html')
    return HttpResponse(template.render())

def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'dev/errorpage.html')

def error(request):
    template = loader.get_template('dev/errorpage.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('dev/landing.html')
    return HttpResponse(template.render())

def generic(request):
    template = loader.get_template('dev/generic.html')
    return HttpResponse(template.render())

def elements(request):
    template = loader.get_template('dev/elements.html')
    return HttpResponse(template.render())

def RubiksCubeSolver(request):
    template = loader.get_template('dev/RubiksCubeSolver.html')
    return HttpResponse(template.render())

def MySociety(request):
    template = loader.get_template('dev/MySociety.html')
    return HttpResponse(template.render())

def BirthdayManager(request):
    template = loader.get_template('dev/BirthdayManager.html')
    return HttpResponse(template.render())

def InvoManager(request):
    template = loader.get_template('dev/InvoManager.html')
    return HttpResponse(template.render())

def Simulation(request):
    template = loader.get_template('dev/Simulation.html')
    return HttpResponse(template.render())

def SudokuSolver(request):
    template = loader.get_template('dev/SudokuSolver.html')
    return HttpResponse(template.render())

def AstroRegister(request):
    template = loader.get_template('dev/AstroRegister.html')
    return HttpResponse(template.render())

def TelescopeAutomation(request):
    template = loader.get_template('dev/TelescopeAutomation.html')
    return HttpResponse(template.render())

