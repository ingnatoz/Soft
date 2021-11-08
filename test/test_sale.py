import pytest
from apps.sale.models import *


@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name='Burguer',
        ean='123456789012',
        sku='1234-bl',
        sale_price='200.23',
        unit_cost='100',
        product_type='Comida'
    )
    assert product.name == 'Burguer'


@pytest.mark.django_db
def test_payment_type_creation():
    payment_type = PaymentType.objects.create(
        name='Tarjeta de Credito',
        sat_code='1234567',
    )
    assert payment_type.name == 'Tarjeta de Credito'


@pytest.mark.django_db
def test_restaurant_creation():
    restaurant = Restaurant.objects.create(
        name='Tarjeta de Credito',
        status=True,
    )
    assert restaurant.status == True


@pytest.mark.django_db
def test_customer_creation():
    customer = Customer.objects.create(
        name='Customer',
        email='customer@test.com',
        rfc='1234',
    )
    assert customer.email == 'customer@test.com'
