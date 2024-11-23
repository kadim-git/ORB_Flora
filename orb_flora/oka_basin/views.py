from django.shortcuts import render

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
# Create your views here.
# catalog/views.py
from django.http import HttpResponse
from .models import Region
from .models import District


class RegionListView(ListView):
    template_name = 'oka_basin/regions.html'
    model = Region

class DistrictListView(ListView):
    template_name = 'oka_basin/districts.html'
    #model = District

    def get_queryset(self):
        self.region = get_object_or_404(Region, name=self.kwargs["region"])
        return District.objects.filter(region_id=self.region.id)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["region"] = self.region
        context["region_list"] = Region.objects.all()
        tt=5
        return context

from flora.models import Reliability    
from flora.models import Species
class SpeciesDistrictListView(ListView):
    template_name = 'oka_basin/speciesindistrict.html'
    
    def get_queryset(self):
        self.region = get_object_or_404(Region, name=self.kwargs["region"])
        self.district = get_object_or_404(District, name=self.kwargs["district"])
        
        spec_list = Species.objects.filter(reliability__district_id__exact=self.district.id, reliability__reliability__gt=0).values_list("name_full", "reliability__district_id", "reliability__reliability")
        spec_list = Reliability.objects.select_related('species_id').filter(district_id__exact=self.district.id, reliability__gt=0)
        
        for s in spec_list:
            tt=55
            print(s)
        return spec_list
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["region"] = self.region
        context["district"] = self.district
        return context