from django.db import models

from django.db import models

class Product(models.Model):
  sku = models.CharField(blank=False, null=False, max_length=200, verbose_name="SKU")
  name = models.CharField(max_length=200)
  brand = models.CharField(max_length=200)

  def __str__(self):
    return self.sku
