from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import viewsets
# Class && Functions
from apps.sale.models import *
from .serializers import *


class PaymentTypeViewSets(viewsets.GenericViewSet):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)


@api_view(['GET', 'POST'])
def payment_type_api_view(request):
    if request.method == 'GET':
        payment_types = SalePaymentType.objects.all()
        if len(payment_types) > 0:
            payment_types_serializer = PaymentTypeSerializer(payment_types, many=True)
            content = {'message': 'success', 'payment_types': payment_types_serializer.data},
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'payment_types': 'payment types not fund...'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        payment_type_serializer = PaymentTypeSerializer(data=request.data)
        if payment_type_serializer.is_valid():
            payment_type_serializer.save()
            content = {'message': "success", 'payment_type': payment_type_serializer.data}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': "errors", 'payment_type': payment_type_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def payment_type_by_id_api_view(request, pk=None):
    payment_type_list = list(PaymentType.objects.filter(id=pk).values())
    if len(payment_type_list) > 0:
        payment_type = SalePaymentType.objects.filter(id=pk).first()
        if request.method == 'GET':
            payment_type_serializer = PaymentTypeSerializer(payment_type)
            content = {'message': "success", 'payment_type': payment_type_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            payment_type_serializer = PaymentTypeSerializer(payment_type, data=request.data)
            if payment_type_serializer.is_valid():
                payment_type_serializer.save()
                content = {'message': "success", 'payment_type': payment_type_serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            content = {'message': "errors", 'payment_type': payment_type_serializer.errors}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            try:
                payment_type.delete()
                return Response({'message': "success"}, status=status.HTTP_200_OK)
            except:
                sale_orders = SaleOrder.objects.filter(payment_type_id=pk).all()
                sale_orders_serializer = SaleOrderSerializer(sale_orders, many=True)
                content = {
                    'message': "errors",
                    'payment_type': "Este Tipo de Pago esta relacionado con alguna/as orden/es de venta/as",
                    'related_sale_orders': sale_orders_serializer.data
                }
                return Response(content, status=status.HTTP_409_CONFLICT)
    else:
        content = {'message': "errors", 'payment_type': "payment type not fund..."}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def customer_api_view(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        if len(customers) > 0:
            customers_serializer = CustomerSerializer(customers, many=True)
            content = {'message': 'success', 'customers': customers_serializer.data},
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'customers': 'customers not fund...'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        customer_serializer = SaleCustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            content = {'message': "success", 'customer': customer_serializer.data}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': "errors", 'customer': customer_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def customer_by_id_api_view(request, pk=None):
    customer_list = list(Customer.objects.filter(id=pk).values())
    if len(customer_list) > 0:
        customer = Customer.objects.filter(id=pk).first()
        if request.method == 'GET':
            customer_serializer = CustomerSerializer(customer)
            content = {'message': "success", 'customer': customer_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            customer_serializer = CustomerSerializer(customer, data=request.data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                content = {'message': "success", 'customer': customer_serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            content = {'message': "errors", 'customer': customer_serializer.errors}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            try:
                customer.delete()
                return Response({'message': "success"}, status=status.HTTP_200_OK)
            except:
                sale_orders = SaleOrder.objects.filter(customer_id=pk).all()
                sale_orders_serializer = SaleOrderSerializer(sale_orders, many=True)
                content = {
                    'message': "errors",
                    'customer': "Este Cliente esta relacionado con alguna/as orden/es de venta/as",
                    'related_sale_orders': sale_orders_serializer.data
                }
                return Response(content, status=status.HTTP_409_CONFLICT)
    else:
        content = {'message': "errors", 'customer': "customer not fund..."}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def restaurant_api_view(request):
    if request.method == 'GET':
        restaurants = SaleChannel.objects.all()
        if len(restaurants) > 0:
            restaurants_serializer = RestaurantSerializer(sale_channels, many=True)
            content = {'message': 'success', 'restaurants': restaurants_serializer.data},
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'restaurants': 'restaurants not fund...'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        sale_channel_serializer = SaleChannelSerializer(data=request.data)
        if sale_channel_serializer.is_valid():
            sale_channel_serializer.save()
            content = {'message': "success", 'sale_channel': sale_channel_serializer.data}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': "errors", 'sale_channel': sale_channel_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sale_channel_by_id_api_view(request, pk=None):
    sale_channel_list = list(SaleChannel.objects.filter(id=pk).values())
    if len(sale_channel_list) > 0:
        sale_channel = SaleChannel.objects.filter(id=pk).first()
        if request.method == 'GET':
            sale_channel_serializer = SaleChannelSerializer(sale_channel)
            content = {'message': "success", 'sale_channel': sale_channel_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            sale_channel_serializer = SaleChannelSerializer(sale_channel, data=request.data)
            if sale_channel_serializer.is_valid():
                sale_channel_serializer.save()
                content = {'message': "success", 'sale_channel': sale_channel_serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            content = {'message': "errors", 'sale_channel': sale_channel_serializer.errors}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            try:
                sale_channel.delete()
                return Response({'message': "success"}, status=status.HTTP_200_OK)
            except:
                sale_orders = SaleOrder.objects.filter(customer_id=pk).all()
                sale_orders_serializer = SaleOrderSerializer(sale_orders, many=True)
                content = {
                    'message': "errors",
                    'customer': "Este Canal de Venta esta relacionado con alguna/as orden/es de venta/as",
                    'related_sale_orders': sale_orders_serializer.data
                }
                return Response(content, status=status.HTTP_409_CONFLICT)
    else:
        content = {'message': "errors", 'sale_channel': "sale channel not fund..."}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
