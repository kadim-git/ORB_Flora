# catalog/urls.py
from django.urls import path

from . import views
from .views import RegionListView
from .views import DistrictListView
from .views import SpeciesDistrictListView

app_name = 'oka_basin'

urlpatterns = [
    #path('old_test', views.regions, name='old_regions'),
    path('', RegionListView.as_view(), name='regions'),
    path('<str:region>/',  DistrictListView.as_view(), name='districts'),
    path('<str:region>/<str:district>/', SpeciesDistrictListView.as_view(), name='species'), 
    # path('<str:family>/<str:ginus>/<slug:species>/', views.speceas_detail),
    # path('2/', views.species_list),
]