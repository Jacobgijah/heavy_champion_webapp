# urls.py
from django.urls import path
from . import views

app_name = "website"

# Link the custom 404 handler
handler404 = 'website.views.custom_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portifolio/', views.portifolio, name='portifolio'),
    path('products/', views.products, name='products'),
    path('product/<str:pid>/', views.product_detail, name='product_detail'),
    path('category/<cid>', views.category, name='category'),
    path('careers/', views.careers, name='careers'),  # New careers page
]
