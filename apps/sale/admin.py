from django.contrib import admin
from .models import *


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name', 'ean', 'sku', 'sale_price', 'unit_cost', 'sat_code', 'product_type', 'status',)
    ordering = ('id',)
    search_fields = ('id', 'name', 'ean', 'sku', 'sale_price', 'unit_cost', 'sat_code', 'product_type', 'status',)
    list_editable = ('name', 'ean', 'sku', 'sale_price', 'unit_cost', 'sat_code', 'product_type', 'status',)
    list_display_links = ('id',)
    list_filter = ('name', 'ean', 'sku', 'sale_price', 'unit_cost', 'sat_code', 'product_type', 'status',)
    list_per_page = 100


@admin.register(PaymentType)
class PaymentType(admin.ModelAdmin):
    list_display = ('id', 'name', 'sat_code',)
    ordering = ('id',)
    search_fields = ('id', 'name', 'sat_code',)
    list_editable = ('name', 'sat_code',)
    list_display_links = ('id',)
    list_filter = ('name', 'sat_code',)
    list_per_page = 100


@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    list_display = ('id', 'name', 'status',)
    ordering = ('id',)
    search_fields = ('id', 'name', 'status',)
    list_editable = ('name', 'status',)
    list_display_links = ('id',)
    list_filter = ('name', 'status',)
    list_per_page = 100


@admin.register(SaleOrder)
class SaleOrder(admin.ModelAdmin):
    list_display = (
        'id', 'marketplace_id', 'total', 'confirm', 'status_order', 'is_fee_retrieve', 'commission', 'user',
        'payment_type', 'restaurant')
    ordering = ('id',)
    search_fields = (
        'id', 'marketplace_id', 'total', 'confirm', 'status_order', 'is_fee_retrieve', 'commission', 'user',
        'payment_type', 'restaurant')
    list_editable = (
        'marketplace_id', 'total', 'confirm', 'status_order', 'is_fee_retrieve', 'commission', 'user', 'payment_type',
        'restaurant')
    list_display_links = ('id',)
    list_filter = ('confirm', 'status_order', 'is_fee_retrieve', 'user', 'payment_type', 'restaurant')
    raw_id_fields = ('payment_type', 'restaurant',)
    list_per_page = 100


@admin.register(SaleOrderProduct)
class SaleOrderProduct(admin.ModelAdmin):
    list_display = (
        'id', 'marketplace_item_id', 'name', 'sku', 'ean', 'quantity', 'price', 'tax', 'shipping_price', 'shipping_tax',
        'shipping_discount', 'discount', 'commission', 'total', 'product', 'sale_order',)
    ordering = ('id',)
    search_fields = (
        'id', 'marketplace_item_id', 'name', 'sku', 'ean', 'quantity', 'price', 'tax', 'shipping_price', 'shipping_tax',
        'shipping_discount', 'discount', 'commission', 'total', 'product', 'sale_order',)
    list_editable = (
        'marketplace_item_id', 'name', 'sku', 'ean', 'quantity', 'price', 'tax', 'shipping_price', 'shipping_tax',
        'shipping_discount', 'discount', 'commission', 'total', 'product', 'sale_order',)
    list_display_links = ('id',)
    list_filter = ('name', 'sku', 'ean', 'product', 'sale_order',)
    raw_id_fields = ('product', 'sale_order',)
    list_per_page = 100
