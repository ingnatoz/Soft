from rest_framework import serializers
from apps.sale.models import SaleOrderProduct


class SaleOrderProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderProduct
        # fields = ['name', 'quantity', 'price', 'total', 'product', ]
        fields = '__all__'
        # exclude = (
        #    'id', 'marketplace_item_id', 'sku', 'ean', 'cost', 'tax', 'shipping_price', 'shipping_tax',
        #    'shipping_discount', 'discount', 'commission', 'sale_order', 'created_at', 'updated_at',
        # )
