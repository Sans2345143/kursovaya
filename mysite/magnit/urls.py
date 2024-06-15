from django.urls import path
from .views import register, login_view, logout_view  # Импортируйте представления из текущего приложения

urlpatterns = [
    path('register/', register, name='register'),  # Используйте пустой путь для регистрации (необязательно)
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Необязательный путь выхода
]