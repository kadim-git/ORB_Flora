from typing import Any
from django.db import models
from django.contrib import admin


# Create your models here.
class Region(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Номер региона')
    name = models.CharField(max_length=30, unique=True, verbose_name='Название региона' )
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    name_en = models.SlugField(blank=True, verbose_name='Название на английском')
    svg_path = models.TextField(blank=True, default='', verbose_name='Границы области, SVG path')

    #@admin.display(ordering="name")
    def __str__(self):
        return self.name

class District(models.Model):
    id = models.IntegerField(primary_key=True)
    region_id = models.ForeignKey(Region, verbose_name="region_name", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True, )
    description = models.TextField(blank=True, default='')
    name_en = models.SlugField(blank=True, verbose_name='Name in English')
    svg_path = models.TextField(blank=True, default='', verbose_name='Границы района, SVG path')

    def __str__(self):
        return self.name
