# serializers.py
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.ListField(write_only=True, required=False)
    category_ids = serializers.ListField(read_only=True, source='categories', child=serializers.IntegerField())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'category_ids']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        product = Product.objects.create(**validated_data)
        for category_name in categories_data:
            category, _ = Category.objects.get_or_create(name=category_name)
            product.categories.add(category)
        return product

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        if categories_data is not None:
            instance.categories.clear()
            for category_name in categories_data:
                category, _ = Category.objects.get_or_create(name=category_name)
                instance.categories.add(category)
        return super().update(instance, validated_data)
