from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(APIView):
    """View для добавления продуктов."""

    def post(self, request):
        serializer = ProductSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProductListView(APIView):
    """View для отображения списка продуктов."""

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products,
            many=True
        )
        return Response(serializer.data)

def index(request):
    """Отображение начальной страницы."""
    return render(request, 'index.html')