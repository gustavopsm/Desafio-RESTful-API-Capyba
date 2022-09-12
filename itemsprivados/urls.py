from django.urls import path
from .views import ItemsPrivados

urlpatterns = [
    path('', ItemsPrivados.as_view(), name='privado')
]