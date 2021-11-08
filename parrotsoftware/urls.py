from django.contrib import admin
from django.urls import path, include, re_path
# Start drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# End drf-yasg
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.views import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="Parrot API",
        default_version='v0.1',
        description="Parrot API documentation",
        terms_of_service="https://miguelvazquez.dev/",
        contact=openapi.Contact(email="ing.miguel.natanael@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/login', Login.as_view(), name='token_login'),
    path('api/logout', Logout.as_view(), name='token_logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', include('apps.users.api.urls')),
    path('api/sale/', include('apps.sale.api.routers')),
    path('api/report/', include('apps.report.api.urls')),
]
