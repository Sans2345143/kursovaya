from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('main/', views.main_view, name='main_view'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('history/', views.history_view, name='history_view'),
    path('generate_qr_code/<str:unique_id>/', views.generate_qr_code, name='generate_qr_code'),
]