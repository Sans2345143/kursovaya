from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),  # URL-шаблон для корневого пути
    path('admin/', admin.site.urls),
    path('page1/', include('magnit.urls')),
    path('page2/', include('magnit.urls')),
]