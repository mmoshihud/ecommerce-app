from rest_framework import serializers

from .models import Category, Brand, Product


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.Serializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"
