from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from product.models import Category
from product.serializers import CategorySerializer


@extend_schema(responses=CategorySerializer)
class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.filter()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
