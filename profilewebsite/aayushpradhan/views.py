from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'errorpage.html')

def error(request):
    template = loader.get_template('errorpage.html')
    return HttpResponse(template.render())

def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render())

def generic(request):
    template = loader.get_template('generic.html')
    return HttpResponse(template.render())

def elements(request):
    template = loader.get_template('elements.html')
    return HttpResponse(template.render())

def RubiksCubeSolver(request):
    template = loader.get_template('RubiksCubeSolver.html')
    return HttpResponse(template.render())

def MySociety(request):
    template = loader.get_template('MySociety.html')
    return HttpResponse(template.render())

def BirthdayManager(request):
    template = loader.get_template('BirthdayManager.html')
    return HttpResponse(template.render())

def InvoManager(request):
    template = loader.get_template('InvoManager.html')
    return HttpResponse(template.render())

def Simulation(request):
    template = loader.get_template('Simulation.html')
    return HttpResponse(template.render())

def SudokuSolver(request):
    template = loader.get_template('SudokuSolver.html')
    return HttpResponse(template.render())

def AstroRegister(request):
    template = loader.get_template('AstroRegister.html')
    return HttpResponse(template.render())

def TelescopeAutomation(request):
    template = loader.get_template('TelescopeAutomation.html')
    return HttpResponse(template.render())
