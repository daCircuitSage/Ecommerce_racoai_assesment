from rest_framework import serializers
from .models import Category
from productsApp.serializers import ProductListSerializer


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id',
                  'name',
                  'image',
                  'products']
        
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'name',
                  'image',
                  'slug']