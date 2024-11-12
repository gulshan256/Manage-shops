from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['osm_id','geometry','brand','city','street','pincode','housenumber','suburb','name','opening_hours','brand_wikipedia','description_de','operator']
    list_filter = ['osm_id','geometry','brand','city','street','pincode','housenumber','suburb','name','opening_hours','brand_wikipedia','description_de','operator']



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    list_filter = ['city_name']