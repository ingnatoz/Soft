from django.db import models
from django.core.validators import *
from .choices import *

numeric_option_a = [MinValueValidator(1), MaxValueValidator(9999999999)]
numeric_option_b = [MinValueValidator(0), MaxValueValidator(9999999999)]
numeric_option_c = [MinValueValidator(0.001), MaxValueValidator(9999999999)]


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, verbose_name='Nombre del Producto')
    ean = models.CharField(max_length=15, null=False, unique=True, verbose_name='EAN')
    sku = models.CharField(max_length=15, null=False, unique=True, verbose_name='SKU')
    sale_price = models.DecimalField(null=False, validators=[MinValueValidator(0)], verbose_name='Precio de Venta',
                                     max_digits=10, decimal_places=2, )
    unit_cost = models.DecimalField(null=False, validators=[MinValueValidator(0)], verbose_name='Costo Unitario',
                                    max_digits=10, decimal_places=2, )
    # img = models.ImageField(null=True, verbose_name='Imagen del Producto')
    sat_code = models.CharField(max_length=20, null=True, blank=True, verbose_name='Codigo del SAT')
    product_type = models.CharField(max_length=50, null=False, verbose_name='Tipo del Producto')
    status = models.BooleanField('Estado', null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, null=True, editable=False, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'product'
        ordering = ['id']

    def product_format(self):
        return "{} / {}".format(self.name, self.sku)

    def __str__(self):
        return self.product_format()


class PaymentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=50, null=False, unique=True, )
    sat_code = models.CharField('Codigo del Sat', max_length=10, null=False, )
    created_at = models.DateTimeField('Creado el', auto_now_add=True, null=True, editable=False, )
    updated_at = models.DateTimeField('Actualizado el', auto_now=True, null=True, editable=False, )

    def payment_type_format(self):
        return "{} / {}".format(self.name, self.sat_code)

    def __str__(self):
        return self.payment_type_format()

    class Meta:
        verbose_name = 'Tipo de Pago'
        verbose_name_plural = 'Tipos de Pago'
        db_table = 'sale_payment_type'
        ordering = ['id']


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=50, null=False, unique=True)
    status = models.BooleanField('Estado', null=False, default=True)
    created_at = models.DateTimeField('Creado el', auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True, null=True, editable=False)

    def restaurant_format(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.restaurant_format()

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'
        db_table = 'restaurant'
        ordering = ['id']


class SaleOrder(models.Model):
    id = models.AutoField(primary_key=True)
    marketplace_id = models.CharField('Marketplace ID', max_length=50, null=False, unique=True)
    total = models.DecimalField('Total', null=False, validators=numeric_option_c, max_digits=10, decimal_places=2, )
    confirm = models.BooleanField('Confirmar', null=False, default=False)
    status_order = models.CharField('Estado de la Orden', max_length=2, null=False, choices=status, default='A', )
    is_fee_retrieve = models.BooleanField('Es deducible', null=False, default=False)
    commission = models.DecimalField('Comisión de la Orden', null=False, default=0, validators=numeric_option_b,
                                     max_digits=10, decimal_places=2, )
    payment_type = models.ForeignKey(PaymentType, null=False, related_name='payment_type_order',
                                     on_delete=models.RESTRICT, verbose_name='Tipo de pago')
    # customer = models.ForeignKey(SaleCustomer, null=False, related_name='customer_order',
    # on_delete=models.RESTRICT, verbose_name='Cliente')
    restaurant = models.ForeignKey(Restaurant, null=False, related_name='channel_order', on_delete=models.RESTRICT,
                                   verbose_name='Canal de Venta')
    created_at = models.DateTimeField('Creado el', auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True, null=True, editable=False)
    delete_at = models.DateTimeField('Eliminado el', null=True, blank=True)

    def sale_order_format(self):
        return "{} / {}".format(self.id, self.marketplace_id)

    def __str__(self):
        return self.sale_order_format()

    class Meta:
        verbose_name = 'Orden de Venta'
        verbose_name_plural = 'Ordenes de Venta'
        db_table = 'sale_order'
        ordering = ['id']


class SaleOrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=250, null=False, )
    sku = models.CharField('SKU', max_length=15, null=True, blank=True, )
    ean = models.CharField('EAN', max_length=15, null=True, blank=True, )
    quantity = models.PositiveBigIntegerField('Cantidad', null=False, validators=numeric_option_a, )
    cost = models.DecimalField('Costo', null=False, validators=numeric_option_b, max_digits=10, decimal_places=2, )
    price = models.DecimalField('Precio de Venta', null=False, validators=numeric_option_c, max_digits=10,
                                decimal_places=2, )
    tax = models.DecimalField('Impuesto', null=False, validators=numeric_option_b, max_digits=10, decimal_places=2, )
    shipping_price = models.DecimalField('Precio de envío', null=False, validators=numeric_option_b, max_digits=10,
                                         decimal_places=2, )
    shipping_tax = models.DecimalField('Impuesto de envío', null=False, validators=numeric_option_b, max_digits=10,
                                       decimal_places=2, )
    shipping_discount = models.DecimalField('Descuento de envío', null=False, validators=numeric_option_b,
                                            max_digits=10, decimal_places=2, )
    discount = models.DecimalField('Descuento', null=False, validators=numeric_option_b, max_digits=10,
                                   decimal_places=2, )
    commission = models.DecimalField('Comisión', null=False, validators=numeric_option_b, max_digits=10,
                                     decimal_places=2, )
    total = models.DecimalField('Total', null=False, validators=numeric_option_c, max_digits=10, decimal_places=2, )
    product = models.ForeignKey(Product, null=False, related_name='product_sale_orders',
                                on_delete=models.RESTRICT, verbose_name='Producto de la Venta')
    sale_order = models.ForeignKey(SaleOrder, null=False, related_name='sale_order_products', on_delete=models.CASCADE,
                                   verbose_name='Orden de Venta')
    marketplace_item_id = models.CharField('Marketplace Item ID', max_length=50, null=True, blank=True, )
    created_at = models.DateTimeField('Creado el', auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True, null=True, editable=False)

    def sale_order_product_format(self):
        return "{} / {}".format(self.id, self.marketplace_item_id)

    def __str__(self):
        return self.sale_order_product_format()

    class Meta:
        verbose_name = 'Producto de la Orden de venta'
        verbose_name_plural = 'Productos de las Ordenes de venta'
        db_table = 'sale_order_product'
        ordering = ['id']
