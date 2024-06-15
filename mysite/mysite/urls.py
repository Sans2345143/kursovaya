from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),  # URL для главного представления
    path('admin/', admin.site.urls),
    path('', include('magnit.urls')),  # Включите URL-адреса приложения magnit в корень
]