from django.shortcuts import render
from website.models import *

def index(request):
  return render(request, "pages/index.html")

def about(request):
  return render(request, "pages/about.html")

def contact(request):
  return render(request, "pages/contact.html")

def portifolio(request):
  query_set = Portifolio.objects.all()
  return render(request, "pages/portifolio.html", {'query_set': query_set})

def products(request):
  products = Product.objects.all()
  return render(request, "pages/products.html", {'products': products})

