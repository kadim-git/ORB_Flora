from django.contrib import admin

# Register your models here.
from .models import Region
from .models import District


admin.site.empty_value_display = 'Не задано' 

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' , 'name_en',)
    search_fields = ('id', 'name',)
    #list_editable =  ( 'name_en',)
    list_display_links = ('id', 'name', ) 
    ordering = ('id',)

    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region_id','name_en',)
    search_fields = ('id', 'name','region_id',) 
    list_display_links = ('id', 'name','region_id', 'name_en')   
    list_filter = ('region_id__name',) 

admin.site.register(Region, RegionAdmin,) 
admin.site.register(District, DistrictAdmin)

