from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path("vhodaition/", views.vhod, name="vhodaition"),
]
