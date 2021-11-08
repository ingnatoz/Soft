from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Avg, Count, Min, Sum

from apps.sale.models import SaleOrderProduct
from apps.report.api.serializers import SaleOrderProductReportSerializer

start_param = openapi.Parameter('start', in_=openapi.IN_QUERY, description='DataTime', type=openapi.TYPE_STRING)
end_param = openapi.Parameter('end', in_=openapi.IN_QUERY, description='DataTime', type=openapi.TYPE_STRING)


@swagger_auto_schema(method='post', manual_parameters=[start_param, end_param], responses={
    200: '{ "message": "success", "sale_order_product": [ {"name": "Daydoku","quantity": 120,"price": 12.0,"total": 100.0,"product": 1,"dcount": 12}]}'})
@api_view(['POST'])
def product_report_api_view(request):
    if request.method == 'POST':
        # try:
        start = (request.data['start'])
        end = request.data['end']
        sale_order_product = SaleOrderProduct.objects.filter(created_at__range=(start, end)) \
            .values('name', 'quantity', 'price', 'total', 'product', ) \
            .annotate(dcount=Count('product')).order_by()
        # .annotate(dcount=Count('product'), quantity_sum=Sum('quantity'), total_sum=Sum('total')).order_by()
    if len(sale_order_product) > 0:
        # sale_order_product_serializer = SaleOrderProductReportSerializer(sale_order_product, many=True)
        content = {'message': 'success', 'sale_order_product': sale_order_product}
        return Response(content, status=status.HTTP_200_OK)
    else:
        content = {'message': 'errors', 'products': 'products not fund...'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    # except:
    #  content = {'message': 'errors', 'products': 'HTTP_400_BAD_REQUEST'}
    #  return Response(content, status=status.HTTP_400_BAD_REQUEST)
