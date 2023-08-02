import pandas as pd
from django.shortcuts import render, redirect
from .forms import CSVUploadForm        #not in use currently : used in upload_csv
from django.http import HttpResponse
from django.template import loader

def WeatherMonitoring(request):
    return render(request, 'dev/weatherbase.html')

def trialform(request):
    return render(request, 'dev/trialform.html')

def result(request):
    try:
        csvfile = request.FILES['cfi']
        df = pd.read_csv(csvfile)
        me = df.mean()
        print('\n\n',me,'\n\n')
        print('\n\n',type(csvfile),'\n\n')
        return render(request, 'dev/result.html', {'cfi': csvfile, 'me': me})
    except TypeError as e:
        error_message = "Error: Invalid CSV file format. Please upload a valid CSV file."
        return render(request, 'dev/error.html', {'error_message': error_message})
    #return render(request, 'dev/result.html', {'cfi': csvfile})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})