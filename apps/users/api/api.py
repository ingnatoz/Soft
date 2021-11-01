from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.sale.models import SaleOrder
from apps.sale.api.serializers import SaleOrderSerializer
from apps.users.api.serializers import UserSerializer, UserListSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        if len(users) > 0:
            users_serializer = UserListSerializer(users, many=True)
            content = {'message': 'success', 'users': users_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'errors', 'users': 'users not fund...'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():  # true or false
            user_serializer.save()
            content = {'message': 'success', 'user': user_serializer.data}
            return Response(content, status=status.HTTP_201_CREATED)
        content = {'message': 'errors', 'user': user_serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_by_id_api_view(request, pk=None):
    users_list = list(User.objects.filter(id=pk).values())
    if len(users_list) > 0:
        user = User.objects.filter(id=pk).first()  # QuerySet
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            content = {'message': 'success', 'user': user_serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            # Este codigo funciona para hacer el Updated al Usuario
            """
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                content = {'message': 'success', 'user': user_serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            """
            content = {'message': 'errors', 'user': 'User not Updated'}
            return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.method == 'DELETE':
            try:
                user.delete()
                return Response({'message': "success"}, status=status.HTTP_200_OK)
            except:
                orders = SaleOrder.objects.filter(user_id=pk).all()
                orders_serializer = SaleOrderSerializer(orders, many=True)
                return Response(
                    {'message': "errors",
                     'user': "Este Usuario esta relacionado con alguna/as orden/es de Venta/as",
                     'related_purchase_orders': orders_serializer.data
                     },
                    status=status.HTTP_409_CONFLICT)
    else:
        return Response({'message': 'errors', 'user': 'user not fund...'}, status=status.HTTP_404_NOT_FOUND)
