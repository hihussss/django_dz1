import os
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'
   
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
   
    msg = " "
    for file in os.listdir():
        msg += f"{file}<br>"   
    return HttpResponse(msg)
