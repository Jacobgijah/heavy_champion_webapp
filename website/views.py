from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from website.models import *


def index(request):
  
  context = {
    
  }

  return render(request, "pages/index.html", context)


def about(request):

  context = {
    

  }

  return render(request, "pages/about.html", context)


def contact(request):
  
  context = {

  }

  return render(request, "pages/contact.html", context)


def portifolio(request):
  query_set = Portifolio.objects.all().order_by("-date")
  
  context = {
    'query_set': query_set,
  }

  return render(request, "pages/portifolio.html", context)


def products(request): 
  products = Product.objects.filter(product_status="published")
  category = Collection.objects.all()

  context = {
    'products': products,
    'category': category
  }

  return render(request, "pages/products.html", context)


def category(request, cid):
  category = Collection.objects.get(cid=cid)
  products = Product.objects.filter(product_status="published", collection=category)

  context = {
    "category": category,
    "products": products,
  }
  return render(request, "pages/category.html", context)