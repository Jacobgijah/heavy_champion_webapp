from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'price', 'collection', 'inventory', 'inventory_status']
  list_editable = ['price']
  list_per_page = 10
  
  @admin.display(ordering='inventory')
  def inventory_status(self, product):
    if product.inventory < 10:
      return 'LOW'
    return 'OK'
  
@admin.register(models.Services)
class ServicesAdmin(admin.ModelAdmin):
  list_display = ['title']
  list_per_page = 10

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_per_page = 10

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
  list_per_page = 10
