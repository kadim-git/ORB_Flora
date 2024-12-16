from django.db import models

from oka_basin.models import District

# Create your models here.
class Family(models.Model):
    index = models.IntegerField(verbose_name='Интекс по Маевскому', null=True, blank=True)
    name = models.CharField(verbose_name="Название, краткое", max_length=30, unique=True, ) #Single word name, can be used in AddressBar
    name_full = models.CharField(max_length=60, verbose_name="Название полное", null=True, blank=True, unique=False )
    name_ru = models.CharField(max_length=60, verbose_name="Название на русском", null=True, blank=True, unique=False)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    distribution = models.TextField(null=True, blank=True, verbose_name="Распространение")
    #slug = models.SlugField(verbose_name='Name for Navigation') #Name for WWW address
    class Meta:
        #ordering = ["index"]
        ordering = ["name"]
    def __str__(self):
        return self.name
    

class Genus(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    index = models.IntegerField(verbose_name='Интекс по Маевскому', null=True, blank=True)
    name = models.CharField(max_length=30, unique=True, verbose_name="Название, краткое" ) #Single word name, can be used in AddressBar
    name_full = models.CharField(max_length=60, null=True, blank=True, unique=False, verbose_name="Название полное" )
    name_ru = models.CharField(max_length=60, null=True, blank=True, unique=False, verbose_name="Название на русском")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    distribution = models.TextField(null=True, blank=True, verbose_name="Распространение")
    #slug = models.SlugField(verbose_name='Name for Navigation') #Name for WWW address
    class Meta:
        #ordering = ["index"]
        ordering = ["name"]
    def __str__(self):
        return self.name

from django.urls import reverse
class Species(models.Model):
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    index = models.IntegerField(verbose_name='Интекс по Маевскому', null=True, blank=True)
    name_short = models.CharField(max_length=30, unique=True, verbose_name="Название, краткое")
    name_full = models.CharField(max_length=60, null=True, blank=True ,unique=False, verbose_name="Название полное" )
    name_syn_lat = models.CharField(max_length=60, null=True, blank=True ,unique=False, verbose_name="Синоним, название научное" )
    name_ru = models.CharField(max_length=50, null=True, blank=True,unique=False, verbose_name="Название на русском")
    name_syn_ru = models.CharField(max_length=50, null=True, blank=True ,unique=False, verbose_name="Синоним, Название на русском" )

    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    distribution = models.TextField(null=True, blank=True, verbose_name="Распространение")
    habitat = models.TextField(null=True, blank=True, verbose_name="Среда обитания")
    WORK_STATUS = [
        (0, "черновик"),
        (1, "в работе"),
        (2, "завершен"),
        ]
    work_status = models.IntegerField(choices=WORK_STATUS, default=0, verbose_name="Рабочий статус")
    
    
    def distribution_str(self):
        citation_link = f"<a href={reverse('flora:families')}>Флора </a>"
        return self.distribution + " TODO for citation ! " + citation_link

    file_reliability = models.FileField(null=True, blank=True,)

    #slug = models.SlugField(verbose_name='Name in English')
    class Meta:
        #ordering = ["index"]
        ordering = ["name_short"]
    
    def __str__(self):
        return self.name_short

    def save(self, **kwargs):
        #do_something()
        pk_if_exist = self.pk
        super().save(**kwargs)  # Call the "real" save() method.
        
        #do_something_else()
        #d1 = District.objects.all()
        if pk_if_exist is None:
            for district_item in District.objects.all():
                #tt=SpeciesDistrict.objects.filter(species_id=55, district_id=district_item).exists()
                Reliability.objects.create(species_id=self, district_id=district_item)
        
        if bool(self.file_reliability) == True:
            print('File is loaded! Process it!')
            
            import xlrd
            book = xlrd.open_workbook(self.file_reliability.path)
            print("The number of worksheets is {0}".format(book.nsheets))
            sh1 = book.sheet_by_index(0)
            spName = sh1.cell_value(rowx=0, colx=3)
            reliab4species = Reliability.objects.filter(species_id__name_short__exact=self.name_short)
            for item in reliab4species:
                index = item.district_id_id
                relVal = sh1.cell_value(rowx=index, colx=3)
                #item.reliability = relVal if relVal is not '' else 0
                try:
                    item.reliability = int(relVal)
                except:
                    item.reliability = 0

                item.save()

            # from openpyxl import Workbook
            # from openpyxl import load_workbook
            # #wb = load_workbook(filename='empty_book.xlsx')
            # wb = load_workbook(filename=self.file_reliability.path)
            # ws=wb['Лист1']
            # for sheet in wb:
            #     print(sheet.title)
            
            # Mat_str = Reliability.objects.filter(species_id__name_short__exact=self.name_short)
            # for dist_Ms in Mat_str:
            #     di1 = f'D{dist_Ms.district_id_id + 1}'
            #     if (re1:=ws[f'D{dist_Ms.district_id_id + 1}'].value) is not None:
            #         dist_Ms.reliability = re1
            #     else:
            #         dist_Ms.reliability = 0
            #     dist_Ms.save()
            
            #self.file_reliability.delete(save=True)
        else:
            print("No file!")
        
    

class Reliability(models.Model): #Reliability of Distribution in the district
    #id = models.IntegerField(primary_key=True)
    RELIABILITY_STATUS = [
        (0, "не отмечен"),
        (1, "наблюдение до 1961г"),
        (2, "наблюдение после 1960г"),
        ( 3, "гербарий до 1961г"),
        ( 4, "гербарий до 1961г и наблюдение после 1960г"),
        ( 5, "гербарий после 1960г"),
    ]
    species_id = models.ForeignKey(Species, verbose_name="species name", on_delete=models.CASCADE)
    district_id = models.ForeignKey(District, verbose_name="district name", on_delete=models.CASCADE,  default=1 )
    reliability = models.IntegerField(choices=RELIABILITY_STATUS, default=0)

    def get_reliability_color(self):
        color_list = ['#ffffff','#eeb467','#c5bf5e','#7da115','#3cac28','#146d2b']
        return color_list[self.reliability]


class Location(models.Model):
    species_id = models.ForeignKey(Species, verbose_name="species name", on_delete=models.CASCADE)
    coordinate_lat_n = models.DecimalField(max_digits=8, decimal_places=6)
    coordinate_long_e = models.DecimalField(max_digits=8, decimal_places=6)
    coordinates_exact = models.BooleanField(default=False) #if coordinates are exact or approximate
    observation_date = models.DateField(blank=True)
    LOCATION_SOURCE = [
        (0, "Гербарий, окроним"),
        (1, "Публикация, данные публикации"),
        ( 2, "INaturalist, ссылка"),
        ( 3, "Наблюдение, карточки, ФИО автора, "),
         ]
    source_type = models.IntegerField(choices=LOCATION_SOURCE, default=0)
    source_info = models.TextField(blank=True)
    description = models.TextField(blank=True)