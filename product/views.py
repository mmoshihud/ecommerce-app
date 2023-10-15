from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from product.models import Category, Brand
from product.serializers import CategorySerializer, BrandSerializer


@extend_schema(responses=CategorySerializer)
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.filter()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.filter()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
