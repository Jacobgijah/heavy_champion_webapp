from django.shortcuts import render
from website.models import *

def index(request):
  # Retrieve the latest price list based on the upload date
  price_list = PriceList.objects.latest('date')

  context = {
    'price_list': price_list,
  }

  return render(request, "pages/index.html", context)

def about(request):
  # Retrieve the latest price list based on the upload date
  price_list = PriceList.objects.latest('date')

  context = {
    'price_list': price_list,
  }

  return render(request, "pages/about.html", context)

def contact(request):
  # Retrieve the latest price list based on the upload date
  price_list = PriceList.objects.latest('date')

  context = {
    'price_list', price_list,
  }

  return render(request, "pages/contact.html", context)

def portifolio(request):
  # Retrieve the latest price list based on the upload date
  price_list = PriceList.objects.latest('date') 
  query_set = Portifolio.objects.all()
  
  context = {
    'price_list': price_list,
    'query_set': query_set,
  }

  return render(request, "pages/portifolio.html", context)

def products(request):
  # Retrieve the latest price list based on the upload date
  price_list = PriceList.objects.latest('date') 
  products = Product.objects.all()

  context = {
    'price_list': price_list,
    'products': products,
  }

  return render(request, "pages/products.html", context)

