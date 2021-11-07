from rest_framework.routers import DefaultRouter

from apps.sale.api.api import *

router = DefaultRouter()

router.register('product', ProductViewSets, basename="product")

urlpatterns = router.urls
