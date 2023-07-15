from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('errorpage', views.error, name='error'),
    #path('errorpage2', views.error2, name='error2'),
    path('landing', views.landing, name='landing'),
    path('generic', views.generic, name='generic'),
    path('elements', views.elements, name='elements'),
    path('RubiksCubeSolver', views.RubiksCubeSolver, name='RubiksCubeSolver'),
    path('MySociety', views.MySociety, name='MySociety'),
    path('BirthdayManager', views.BirthdayManager, name='BirthdayManager'),
    path('InvoManager', views.InvoManager, name='InvoManager'),
    path('Simulation', views.Simulation, name='Simulation'),
    path('SudokuSolver', views.SudokuSolver, name='SudokuSolver'),
    path('AstroRegister', views.AstroRegister, name='AstroRegister'),
    path('TelescopeAutomation', views.TelescopeAutomation, name='TelescopeAutomation'),
]