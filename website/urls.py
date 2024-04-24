from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('portifolio/',views.portifolio, name='portifolio'),
    path('products/',views.products, name='products'),
    path('category/<int:id>',views.category, name='category'),
]