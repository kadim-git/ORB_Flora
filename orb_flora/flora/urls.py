# catalog/urls.py
from django.urls import path

from . import views

app_name = 'flora'

urlpatterns = [
    path('', views.families, name='families'),
    path('<str:family>/', views.genera, name='genera'),
    path('<str:family>/<str:genus>/', views.species, name='species'),
    path('<str:family>/<str:genus>/<str:species>/', views.species_detail, name='species_detail'),
    
    # path('<str:family>/<str:ginus>/<slug:species>/', views.speceas_detail),
    # path('2/', views.species_list),
]