# homepage/urls.py

# Импортируем функцию path() 
# и файл homepage/views.py, в котором объявлена view-функция index().
from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
]