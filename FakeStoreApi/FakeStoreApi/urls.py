from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/', include('api.urls'))
]
