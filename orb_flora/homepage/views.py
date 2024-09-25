from django.shortcuts import render

# Create your views here.
# catalog/views.py
from django.http import HttpResponse

def index(request):
    template = 'homepage/index.html'
    return render(request, template)