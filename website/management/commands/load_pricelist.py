from django.core.management.base import BaseCommand
from website.models import PriceList

class Command(BaseCommand):
    help = 'Load data into the PriceList table'

    def handle(self, *args, **kwargs):
        # Define the data to be loaded
        data = [
            {"title": "Product Price List 1", "file": "doc/priceList.txt"},
        ]

        # Load the data into the PriceList table
        for item in data:
            PriceList.objects.create(title=item["title"], file=item["file"])

        self.stdout.write(self.style.SUCCESS('Successfully loaded data into PriceList table'))
