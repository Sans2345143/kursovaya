from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# Простая функция для домашней страницы

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('magnit.urls')),  # assuming your app is named 'your_app'
]
