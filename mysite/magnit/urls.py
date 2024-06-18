from django.urls import path
from .views import get_products, get_stats
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main_view'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('generate-qr/<str:unique_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('products/', get_products, name='products'),
    path('statistics/', get_stats, name='statistics'),
]