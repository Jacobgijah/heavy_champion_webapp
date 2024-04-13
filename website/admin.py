from typing import Any
from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'price', 'inventory', 'inventory_status', 'collection_title']
  list_editable = ['price']
  list_per_page = 10
  list_select_related = ['collection']
  
  def collection_title(self, product):
    return product.collection.title
  
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
  list_display = ['title', 'products_count']
  list_per_page = 10

  @admin.display(ordering='products_count')
  def products_count(self, collection):
    return collection.products_count
  
  def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    return super().get_queryset(request).annotate(
      products_count=Count('product')
    )

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
  list_per_page = 10
