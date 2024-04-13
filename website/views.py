from django.shortcuts import render
from website.models import *

def index(request):
  return render(request, "pages/index.html")

def about(request):
  return render(request, "pages/about.html")

def contact(request):
  return render(request, "pages/contact.html")

def services(request):
  services = Services.objects.all()
  return render(request, "pages/services.html", {'services': services})

def products(request):
  products = Product.objects.all()
  return render(request, "pages/products.html", {'products': products})

