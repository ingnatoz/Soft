from rest_framework.routers import DefaultRouter
from apps.sale.api.api import PaymentTypeViewSets

router = DefaultRouter()
router.register('payment_type', PaymentTypeViewSets, basename='payment_type', )
urlpatterns = router.urls
