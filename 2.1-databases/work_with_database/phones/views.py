from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_name = request.GET.get("sort")
    if sort_name == "name":
        phones_obj = Phone.objects.order_by("name")
    elif sort_name == "min_price":
        phones_obj = Phone.objects.order_by("price")
    elif sort_name == "max_price":
        phones_obj = Phone.objects.order_by("-price")
    else:
        phones_obj = Phone.objects.all()    
    context = {
        'phones': phones_obj
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    
    return render(request, template, context)
