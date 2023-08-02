from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeatherMonitoring, name='WeatherMonitoring'),
    path('result', views.result, name='result'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    #path('trialform', views.show, name='trialform'),
]