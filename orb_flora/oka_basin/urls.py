# catalog/urls.py
from django.urls import path

from . import views

app_name = 'oka_basin'

urlpatterns = [
    path('', views.regions, name='regions'),

    #path('<str:family>/', views.genera_list),
    #path('<str:family>/<str:genus>/', views.species_list), 
    # path('<str:family>/<str:ginus>/<slug:species>/', views.speceas_detail),
    # path('2/', views.species_list),
]