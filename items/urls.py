from django.urls import path
from .views import Items

urlpatterns = [
    path('', Items.as_view(), name='items'),
]