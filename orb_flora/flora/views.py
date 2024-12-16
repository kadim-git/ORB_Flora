from django.shortcuts import render

# Create your views here.

# catalog/views.py
from django.http import HttpResponse
from .models import Family
from .models import Genus
from .models import Species
from .models import Reliability
from .models import Location

def species_detail(request, family, genus, species):
    template = 'flora/detail.html'
    
    species_info = Species.objects.get(name_short__exact=species)
    reliability_list = Reliability.objects.filter(species_id__exact=species_info.pk).select_related('district_id','district_id__region_id')
    location_list = Location.objects.filter(species_id__exact=species_info.pk)
    context = {"family": family, 
                "genus": genus, 
                "species": species_info, 
                "reliability_list": reliability_list,
                "location_list": location_list}
    return render(request, template, context)

def families(request):
    template = 'flora/families.html'
    
    families_list = Family.objects.values('name', 'name_full', 'name_ru', 'index').order_by('name')
    context = {'families_list': families_list, }

    return render(request, template, context)


def genera(request, family):
    template = 'flora/genera.html'
    
    family = Family.objects.get(name=family)
    genera_list = Genus.objects.values('name', 'name_full', 'name_ru', 'index', 'description', 'distribution').filter(family__name__exact=family).order_by('name')
   
    context = {
        "family": family, 
        'genera_list': genera_list, }
    return render(request, template, context)
 

def species(request, family, genus):
    template = 'flora/species.html'
    
    species_list = Species.objects.values('name_short', 'name_full', 'name_ru', 'pk').filter(genus__name__exact=genus).order_by('pk')

    context = {
        "family": family, 
        "genus": genus,
        'species_list': species_list, }
    print(type(context))
    return render(request, template, context)
    