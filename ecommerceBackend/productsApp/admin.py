from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sku',
        'price',
        'stock',
        'featured'
    )
admin.site.register(Product, ProductAdmin)
