from django.db import models
from categoriesApp.models import Category
from django.utils.text import slugify
import random


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='product_img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,related_name='products', blank=True, null=True)
    # Using 'featured' (True/False) instead of a status (active/inactive) field
    featured = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        #featured control---
        if self.stock <= 0:
            self.featured = False
        else:
            self.featured = True

        #slug generation---
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1

            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        #SKU generation---
        if not self.sku:
            base_sku = "".join(c for c in self.name.upper() if c.isalnum())
            while True:
                random_number = random.randint(100,999)
                sku = f'{base_sku}-{random_number}'
                if not Product.objects.filter(sku=sku).exists():
                    self.sku = sku
                    break
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
