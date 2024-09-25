from django.contrib import admin

# Register your models here.
from .models import Family
from .models import Species
from .models import Reliability
from .models import Location
from .models import Genus
from oka_basin.models import District

admin.site.site_header = "Щербаков, администрирование"

admin.site.empty_value_display = 'Не задано' 

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('index', 'name', 'name_full', 'name_ru' )
    sortable_by = ( 'name', 'name_ru' )
    list_display_links = ('index', 'name', 'name_full', 'name_ru' )
    search_fields = ('index', 'name', 'name_full', 'name_ru' )
    
admin.site.register(Family, FamilyAdmin)


class GenusAdmin(admin.ModelAdmin):
    list_display = ('index','name', 'name_full', 'name_ru' , 'family',)
    list_display_links = ('index','name', 'name_full', 'name_ru' , 'family')
    search_fields = ('index','name', 'name_full', 'name_ru' , 'family')
    list_filter = ('family__name_full',)

admin.site.register(Genus, GenusAdmin)
    
class ReliabilityInline(admin.TabularInline):
    model = Reliability
    extra = 0

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1

@admin.action(description="Set to 0 (Import Reliability from .xls file)")
def import_reliability(modeladmin, request, queryset):
    for obj in queryset:
        print(obj)
        reliab4spec = Reliability.objects.filter(species_id__exact=obj.pk)
        for item in reliab4spec:
            item.reliability = 0
            item.save()
        #queryset.update(status="p")


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'index', 'name_short', 'genus', 'name_ru',  'work_status','file_reliability')
    list_editable = ('file_reliability',)
    search_fields = ('index', 'name_short', 'name_full',) 
    list_display_links = ('index', 'name_short','name_ru', )  
    list_filter = ('genus__name', 'genus__family')
    inlines = [ReliabilityInline, LocationInline]
    actions = (import_reliability,)


class ReliabilityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'species_id', 'district_id', 'reliability')
    list_display_links = ('pk', 'species_id', 'district_id', 'reliability')  
    list_filter = ["species_id"]  
    radio_fields = {"reliability": admin.VERTICAL}

class LocationAdmin(admin.ModelAdmin):
    list_display = ('species_id', 'coordinate_lat_n', 'coordinate_long_e', 'observation_date', 'source_type' )
    list_display_links = ('species_id', 'coordinate_lat_n', 'coordinate_long_e', 'observation_date' )


admin.site.register(Species, SpeciesAdmin) 
admin.site.register(Reliability, ReliabilityAdmin)
admin.site.register(Location, LocationAdmin)

