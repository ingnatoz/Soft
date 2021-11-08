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
        return Response(product_serializer.data, status=status.HTTP_200_OK)

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
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The product you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)


class PaymentTypeViewSets(viewsets.GenericViewSet):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    list_serializer_class = PaymentTypeSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        payment_type = self.get_queryset()
        payment_type_serializer = self.list_serializer_class(payment_type, many=True)
        return Response(payment_type_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        payment_type_serializer = self.serializer_class(data=request.data)
        if payment_type_serializer.is_valid():
            payment_type_serializer.save()
            return Response({
                'message': 'Payment Type registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': product_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        payment_type = self.get_object(pk)
        payment_type_serializer = self.serializer_class(payment_type)
        return Response(payment_type_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        payment_type = self.get_object(pk)
        payment_type_serializer = PaymentTypeSerializer(payment_type, data=request.data)
        if payment_type_serializer.is_valid():
            payment_type_serializer.save()
            return Response({
                'message': 'Payment Type updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': payment_type_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment_type_list = list(self.model.objects.filter(id=pk).values())
        if len(payment_type_list) > 0:
            payment_type = self.model.objects.filter(id=pk).first()
            payment_type.delete()
            return Response({
                'message': 'Payment Type deleted successfully.'
            })
        return Response({
            'message': 'The Payment Type you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)


class RestaurantViewSets(viewsets.GenericViewSet):
    model = Restaurant
    serializer_class = RestaurantSerializer
    list_serializer_class = RestaurantSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        restaurant = self.get_queryset()
        restaurant_serializer = self.list_serializer_class(restaurant, many=True)
        return Response(restaurant_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        restaurant_serializer = self.serializer_class(data=request.data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return Response({
                'message': 'Restaurant registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': restaurant_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        restaurant = self.get_object(pk)
        restaurant_serializer = self.serializer_class(restaurant)
        return Response(restaurant_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        restaurant = self.get_object(pk)
        restaurant_serializer = RestaurantSerializer(restaurant, data=request.data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return Response({
                'message': 'Restaurant updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': restaurant_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        restaurant_list = list(self.model.objects.filter(id=pk).values())
        if len(restaurant_list) > 0:
            restaurant = self.model.objects.filter(id=pk).first()
            restaurant.delete()
            return Response({
                'message': 'Restaurant deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Payment Type you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)


class CustomerViewSets(viewsets.GenericViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    list_serializer_class = CustomerSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        customer = self.get_queryset()
        customer_serializer = self.list_serializer_class(customer, many=True)
        return Response(customer_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        customer_serializer = self.serializer_class(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response({
                'message': 'Customer registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': customer_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        customer = self.get_object(pk)
        customer_serializer = self.serializer_class(customer)
        return Response(customer_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        customer = self.get_object(pk)
        customer_serializer = CustomerSerializer(customer, data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response({
                'message': 'Customer updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': customer_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        customer_list = list(self.model.objects.filter(id=pk).values())
        if len(customer_list) > 0:
            customer = self.model.objects.filter(id=pk).first()
            customer.delete()
            return Response({
                'message': 'Customer deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Payment Type you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)


class SaleOrderViewSets(viewsets.GenericViewSet):
    model = SaleOrder
    serializer_class = SaleOrderSerializer
    list_serializer_class = SaleOrderSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        sale_order = self.get_queryset()
        sale_order_serializer = self.list_serializer_class(sale_order, many=True)
        return Response(sale_order_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        sale_order_serializer = self.serializer_class(data=request.data)
        if sale_order_serializer.is_valid():
            sale_order_serializer.save()
            return Response({
                'message': 'Sale Order registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': sale_order_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sale_order = self.get_object(pk)
        sale_order_serializer = self.serializer_class(sale_order)
        return Response(sale_order_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        sale_order = self.get_object(pk)
        sale_order_serializer = SaleOrderSerializer(sale_order, data=request.data)
        if sale_order_serializer.is_valid():
            sale_order_serializer.save()
            return Response({
                'message': 'Sale Order updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': sale_order_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        sale_order_list = list(self.model.objects.filter(id=pk).values())
        if len(sale_order_list) > 0:
            sale_order = self.model.objects.filter(id=pk).first()
            sale_order.delete()
            return Response({
                'message': 'Sale Order deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Sale Order you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)


class SaleOrderProductSViewSets(viewsets.GenericViewSet):
    model = SaleOrderProduct
    serializer_class = SaleOrderProductSerializer
    list_serializer_class = SaleOrderProductSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        sale_order_product = self.get_queryset()
        sale_order_product_serializer = self.list_serializer_class(sale_order_product, many=True)
        return Response(sale_order_product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        sale_order_product_serializer = self.serializer_class(data=request.data)
        if sale_order_product_serializer.is_valid():
            sale_order_product_serializer.save()
            return Response({
                'message': 'Sale Order Product registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': sale_order_product_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sale_order_product = self.get_object(pk)
        sale_order_product_serializer = self.serializer_class(sale_order_product)
        return Response(sale_order_product_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        sale_order_product = self.get_object(pk)
        sale_order_product_serializer = SaleOrderProductSerializer(sale_order_product, data=request.data)
        if sale_order_product_serializer.is_valid():
            sale_order_product_serializer.save()
            return Response({
                'message': 'Sale Order Product updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': sale_order_product_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        sale_order_product_list = list(self.model.objects.filter(id=pk).values())
        if len(sale_order_product_list) > 0:
            sale_order_product = self.model.objects.filter(id=pk).first()
            sale_order_product.delete()
            return Response({
                'message': 'Sale Order Product deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Sale Order Product you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)
