from django.shortcuts import render

# Create your views here.
# catalog/views.py
from django.http import HttpResponse

def regions(request):
    template = 'oka_basin/description.html'
    return render(request, template)