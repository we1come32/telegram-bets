from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bets/', include('Bets.urls')),
    path('auth/', include('AUTH.urls')),
    path('api/', include('rest_framework.urls')),
    path('auth/', include('API.urls')),
    path('', include('Default.urls')),
]
