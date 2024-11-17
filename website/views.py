from django.db.models import Count
from django.core.paginator import Paginator
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
    # Default sorting by most recently uploaded
    sort = request.GET.get('sort', '-created_at')  # Get sort parameter or use default
    products = Product.objects.filter(product_status="published").order_by(sort)
    category = Collection.objects.all()

    # Pagination setup: 9 products per page
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Check if there are any published products
    no_products = not products.exists()

    context = {
        'page_obj': page_obj,
        'category': category,
        'sort': sort,  # Pass the sort parameter to the template
        'no_products': no_products,  # Add a flag for no products
    }

    return render(request, "pages/product/products.html", context)


def product_detail(request, pid):
    # Fetch the product using the unique pid
    product = get_object_or_404(Product, pid=pid)

    # Fetch additional images for the product
    product_images = ProductImages.objects.filter(product=product)

    whatsapp_number = "255758248415"

    context = {
        'product': product,
        'product_images': product_images,
        'whatsapp_number': whatsapp_number,
    }

    return render(request, "pages/product/product_detail.html", context)



def category(request, cid):
  category = Collection.objects.get(cid=cid)
  products = Product.objects.filter(product_status="published", collection=category)

  context = {
    "category": category,
    "products": products,
  }
  return render(request, "pages/category.html", context)


def careers(request):
    # This is a simple view, you can expand it later to add dynamic data
    context = {
        'message': "This page is under development"
    }
    return render(request, "pages/careers.html", context)


# Add the custom 404 view
def custom_404(request, exception=None):
  return render(request, '404.html', status=404)