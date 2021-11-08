from django.urls import path
from apps.report.api.api import product_report_api_view

urlpatterns = [
    path('product', product_report_api_view, name='product'),
]
