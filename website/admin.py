from django.contrib import admin
from website.models import *

class ProductImagesAdmin(admin.TabularInline):
  model = ProductImages



class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImagesAdmin]
  list_display = ['title', 'product_image', 'price', 'featured', 'product_status']
  list_editable = ['product_status']



class CollectionAdmin(admin.ModelAdmin):
  list_display = ['title', 'featured_product']
  list_editable = ['title']
  list_display_links = ['featured_product']


class VendorAdmin(admin.ModelAdmin):
  list_display = ['title', 'image']


class PortifolioImagesAdmin(admin.TabularInline):
  model = PortifolioImages


class PortifolioAdmin(admin.ModelAdmin):
  inlines = [PortifolioImagesAdmin]
  list_display = ['title', 'description']


class PriceListAdmin(admin.ModelAdmin):
  list_display = ['title', 'file']



admin.site.register(Collection, CollectionAdmin)
admin.site.register(Portifolio, PortifolioAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor, VendorAdmin)