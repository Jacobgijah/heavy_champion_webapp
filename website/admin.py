from typing import Any
from django.db.models.aggregates import Count
from django.contrib import admin
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

class InventoryFilter(admin.SimpleListFilter):
  title = 'inventory'
  parameter_name = 'inventory'
  
  def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
    return [
      ('<20', 'Low')
    ]
    
  def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
    if self.value() == '<20':
      return queryset.filter(inventory__lt=20)
  
  
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'price', 'inventory_status', 'collection_title']
  list_editable = ['price']
  list_filter = ['collection', 'last_update', InventoryFilter]
  list_per_page = 10
  list_select_related = ['collection']
  search_fields = ['title']
  
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
  search_fields = ['title']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['title', 'products_count']
  list_per_page = 10

  @admin.display(ordering='products_count')
  def products_count(self, collection):
    url = (
            reverse('admin:website_product_changelist') 
            + '?'
            + urlencode({
              'collection__id': str(collection.id)
            }))
    return format_html('<a href="{}">{}</a>', url, collection.products_count)
  
  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      products_count=Count('product')
    )

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
  list_per_page = 10
