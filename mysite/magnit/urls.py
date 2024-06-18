from .views import register, login_view, logout_view, main_view # Import all view functions
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('main_view/', main_view, name='main_view'),
    path('logout/', logout_view, name='logout'),
    path('generate_qr_code/<unique_id>/', views.generate_qr_code, name='generate_qr_code'),
]