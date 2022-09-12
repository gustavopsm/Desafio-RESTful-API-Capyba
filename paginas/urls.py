from django.urls import path
from .views import Inicio, Menu

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('menu', Menu.as_view(), name='menu'),

]