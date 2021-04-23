from django.contrib import admin
from publicapp.models import *

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name','prize','image')

class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name','prize','image') 

class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('name','prize','image')

class GrocerieAdmin(admin.ModelAdmin):
    list_display = ('name','prize','image')           

# Register your models here.
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Electronic, ElectronicAdmin)
admin.site.register(Grocerie, GrocerieAdmin)