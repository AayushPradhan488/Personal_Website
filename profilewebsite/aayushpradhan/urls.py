from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('errorpage', views.error, name='error'),
    path('landing', views.landing, name='landing'),
    path('generic', views.generic, name='generic'),
    path('elements', views.elements, name='elements'),
]