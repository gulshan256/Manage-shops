from django.db import models
from multiselectfield import MultiSelectField
from .config import *


# Create your models here.



class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'City'

    def __str__(self):
        return self.city_name
    
    



Brand_choices = ((brand.lower(), brand.title()) for brand in BRAND_CHOICES)


class Brand(models.Model):
    osm_id=models.CharField(max_length=20)
    geometry=models.CharField(max_length=100, null=True, blank=True)
    brand=models.CharField(max_length=100, null=True, blank=True, choices=Brand_choices)
    city=models.CharField(max_length=100, null=True, blank=True)
    street=models.CharField(max_length=100, null=True, blank=True)
    pincode=models.CharField(max_length=100, null=True, blank=True)
    housenumber=models.CharField(max_length=100, null=True, blank=True)
    suburb=models.CharField(max_length=100, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    opening_hours=models.CharField(max_length=100, null=True, blank=True)
    brand_wikipedia=models.TextField(null=True, blank=True)
    description_de=models.TextField(null=True, blank=True)
    operator=models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'Brand'



# dynamic_form/models.py


class DynamicFormModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
