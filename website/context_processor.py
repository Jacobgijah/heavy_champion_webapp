from django.shortcuts import get_object_or_404
from website.models import *


def default(request):
  # Retrieve the latest price list based on the upload date
  price_list = get_object_or_404(PriceList.objects.order_by("-date"))

  return {
    "price_list": price_list,
  }