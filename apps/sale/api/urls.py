from django.urls import path
from apps.sale.api.api import *

urlpatterns = [
    path('payment_type', payment_type_api_view, name='payment_type_api_view'),
    path('payment_type/<int:pk>', payment_type_by_id_api_view, name='payment_type_by_id_api_view'),
    path('customer', customer_api_view, name='customer_api_view'),
    path('customer/<int:pk>', customer_by_id_api_view, name='customer_by_id_api_view'),
    path('sale_channel', sale_channel_api_view, name='sale_channel_api_view'),
    path('sale_channel/<int:pk>', sale_channel_by_id_api_view, name='sale_channel_by_id_api_view'),
]
