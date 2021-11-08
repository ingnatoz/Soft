from rest_framework.routers import DefaultRouter

from apps.sale.api.api import *

router = DefaultRouter()

router.register('product', ProductViewSets, basename="product")
router.register('payment_type', PaymentTypeViewSets, basename="payment_type")
router.register('restaurant', RestaurantViewSets, basename="restaurant")
router.register('customer', CustomerViewSets, basename="customer")
router.register('order', SaleOrderViewSets, basename="sale_order")
router.register('order_product', SaleOrderProductSViewSets, basename="sale_order_product")

urlpatterns = router.urls
