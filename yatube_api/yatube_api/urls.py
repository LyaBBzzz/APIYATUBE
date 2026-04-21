from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Yatube API",
      default_version='v1',
      description="Документация API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/users/', include('api.user_urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/jwt/create/', TokenObtainPairView.as_view()),
    path('api/v1/jwt/refresh/', TokenRefreshView.as_view()),
    path('api/v1/jwt/verify/', TokenVerifyView.as_view()),
]

urlpatterns += [
    re_path(r'^swagger/$', schema_view.with_ui('swagger')),
    re_path(r'^redoc/$', schema_view.with_ui('redoc')),
]