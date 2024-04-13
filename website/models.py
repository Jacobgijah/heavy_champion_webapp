from django.db import models

class Promotion(models.Model):
  description = models.CharField(max_length=255)
  discount = models.FloatField()
class Collection(models.Model):
  title = models.CharField(max_length=255)
  featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,
                                       null=True, related_name='+')
class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  promotions = models.ManyToManyField(Promotion)

class Services(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()