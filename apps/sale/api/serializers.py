from rest_framework import serializers
from apps.sale.models import Product, PaymentType, Restaurant, Customer, SaleOrder, SaleOrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'


class SaleOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderProduct
        fields = '__all__'
