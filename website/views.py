from django import forms
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.conf import settings
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


# Define the ContactForm class
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter your name'}),
        label="Name",
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter your email'}),
        label="Email",
    )
    phone = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(r'^0[67]\d{8}$', message="Phone number must start with 06 or 07 and be 10 digits.")
        ],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter your phone number'}),
        label="Phone",
    )
    message = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter your message', 'rows': 3}),
        label="Message",
    )



# Contact view
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            try:
                # Attempt to send an email
                send_mail(
                    subject=f"Contact Form Submission by {name}",
                    message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
                    from_email=settings.EMAIL_HOST_USER,  # Use the configured sender's email address
                    recipient_list=['jacobgijjah@gmail.com'],
                    fail_silently=False,  # Set to False to debug errors during email sending
                )
                response_message = "Your message has been sent successfully!"
                response_status = "success"
                
                # Clear the form after submission
                form = ContactForm()  # Reset the form instance after successful submission

            except Exception as e:
                response_message = "Failed to send your message. Please try again later."
                response_status = "error"
        else:
            response_message = "Please correct the errors in the form."
            response_status = "error"
    else:
        form = ContactForm()
        response_message = None
        response_status = None

    return render(request, "pages/contact.html", {
        'form': form,
        'response_message': response_message,
        'response_status': response_status,
    })



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