import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    
    with open('./data-398-2018-08-30.csv', newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        bus = [row for row in reader]
        
    page_number = request.GET.get('page',1)  
    paginator = Paginator(bus, 10)
    
    page = paginator.get_page(page_number)
    
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
