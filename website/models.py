from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField

STATUS_CHOICES = (
  ("process", "Processing"),
  ("shipped", "Shipped"),
  ("delivered", "Delivered"),
)

STATUS = (
  ("draft", "Draft"),
  ("disabled", "Disabled"),
  ("rejected", "Rejected"),
  ("in_review", "In Review"),
  ("published", "Published"),
)

RATING = (
  (1, "★☆☆☆☆"),
  (2, "★★☆☆☆"),
  (3, "★★★☆☆"),
  (4, "★★★★☆"),
  (5, "★★★★★"),
)

class Collection(models.Model):
  cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")
  title = models.CharField(max_length=255, default="Biomedical")
  featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='+')
  
  class Meta:
    ordering = ['title']
  
  def __str__(self) -> str:
    return self.title

class Vendor(models.Model):
  vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
  title = models.CharField(max_length=100, default="Vendor")
  image = models.ImageField(upload_to="vendor-images", default="vendor.jpg")
  description = models.TextField(null=True, blank=True)
  address = models.CharField(max_length=100, default="10 Kinondoni Dar es Salaam")
  contact = models.CharField(max_length=100, default="+255 000 000 000")
  chat_resp_time = models.CharField(max_length=100, default=100)
  shipping_on_time = models.CharField(max_length=100, default=100)
  authentic_rating = models.CharField(max_length=100, default=100)
  days_return = models.CharField(max_length=100, default=100)
  warranty_period = models.CharField(max_length=100, default=100)


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")
    collection = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Product")
    slug = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='avatar.png', upload_to='product_images')
    long_description = models.TextField(null=True, blank=True, default="This is a product")
    short_description = models.CharField(max_length=255, null=True, blank=True, default="Short product description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="10000.00", validators=[MinValueValidator(100)])
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default="20000.00", validators=[MinValueValidator(100)])
    specifications = models.TextField(null=True, blank=True)
    product_status = models.CharField(max_length=10, choices=STATUS, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self) -> str:
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProductImages(models.Model):
  images = models.ImageField(upload_to="product-images", default="product.jpg")
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = "Product Images"

class Portifolio(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=255)
  image = models.ImageField(default='portifolio.jpg', upload_to='portifolio_images')
  description = models.TextField()
  
  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering = ['-date']


class PortifolioImages(models.Model):
  images = models.ImageField(upload_to="Portifolio-images", default="portifolio.jpg")
  portifolio = models.ForeignKey(Portifolio, on_delete=models.CASCADE, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = "Portifolio Images"


class PriceList(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=255, default="Product Price List")
  file = models.FileField(upload_to='doc', default="priceList.txt")

  def __str__(self) -> str:
    return self.title
