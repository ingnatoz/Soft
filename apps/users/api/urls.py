from django.urls import path
from apps.users.api.api import *

urlpatterns = [
    path('user', user_api_view, name='user_api_view'),
    path('user/<int:pk>', user_by_id_api_view, name='user_by_id_api_view'),
]
