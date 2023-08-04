from django.contrib import admin
from .models import Product,Categorys
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','date_add']
    ordering = ('name',)

@admin.register(Categorys)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)
