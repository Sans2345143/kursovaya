from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('magnit.urls')),  # Включите URL-адреса приложения magnit в корень
]