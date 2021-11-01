from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.views import Login, Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', Login.as_view(), name='token_login'),
    path('api/logout', Logout.as_view(), name='token_logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('apps.users.api.urls')),
]
