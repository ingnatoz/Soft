# Python
# Django
# Third
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Class && Functions
from apps.purchase.models import PurchaseProduct
from apps.sale.models import *
from .serializers import *


@api_view(['GET', 'POST'])
def payment_type_api_view(request):
    if request.method == 'GET':
        payment_types = SalePaymentType.objects.all()
        if len(payment_types) > 0:
            payment_types_serializer = SalePaymentTypeSerializer(payment_types, many=True)
            content = {'message': 'success', 'payment_types': payment_types_serializer.data},
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'payment_types': 'payment types not fund...'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        payment_type_serializer = SalePaymentTypeSerializer(data=request.data)
        if payment_type_serializer.is_valid():
            payment_type_serializer.save()
            content = {'message': "success", 'payment_type': payment_type_serializer.data}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': "errors", 'payment_type': payment_type_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def payment_type_by_id_api_view(request, pk=None):
    payment_type_list = list(SalePaymentType.objects.filter(id=pk).values())
    if len(payment_type_list) > 0:
        payment_type = SalePaymentType.objects.filter(id=pk).first()
        if request.method == 'GET':
            payment_type_serializer = SalePaymentTypeSerializer(payment_type)
            content = {'message': "success", 'payment_type': payment_type_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            payment_type_serializer = SalePaymentTypeSerializer(payment_type, data=request.data)
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
        customers = SaleCustomer.objects.all()
        if len(customers) > 0:
            customers_serializer = SaleCustomerSerializer(customers, many=True)
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
    customer_list = list(SaleCustomer.objects.filter(id=pk).values())
    if len(customer_list) > 0:
        customer = SaleCustomer.objects.filter(id=pk).first()
        if request.method == 'GET':
            customer_serializer = SaleCustomerSerializer(customer)
            content = {'message': "success", 'customer': customer_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            customer_serializer = SaleCustomerSerializer(customer, data=request.data)
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
def sale_channel_api_view(request):
    if request.method == 'GET':
        sale_channels = SaleChannel.objects.all()
        if len(sale_channels) > 0:
            sale_channels_serializer = SaleChannelSerializer(sale_channels, many=True)
            content = {'message': 'success', 'sale_channels': sale_channels_serializer.data},
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'sale_channels': 'sale channels not fund...'}
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