from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

from apps.sale.models import Product, PaymentType, Restaurant, Customer, SaleOrder, SaleOrderProduct
from .serializers import *


class ProductViewSets(viewsets.GenericViewSet):
    model = Product
    serializer_class = ProductSerializer
    list_serializer_class = ProductSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        product = self.get_queryset()
        product_serializer = self.list_serializer_class(product, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        product_serializer = self.serializer_class(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({
                'message': 'Product registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': product_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_object(pk)
        product_serializer = self.serializer_class(product)
        return Response(product_serializer.data)

    def update(self, request, pk=None):
        product = self.get_object(pk)
        product_serializer = ProductSerializer(product, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({
                'message': 'Product updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': product_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product_destroy = self.model.objects.filter(id=pk).update(status=False)
        if product_destroy == 1:
            return Response({
                'message': 'Product deleted successfully.'
            })
        return Response({
            'message': 'The product you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)
