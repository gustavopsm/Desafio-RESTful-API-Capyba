from .models import Item
from .serializers import ItemSerializer
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .povoar import povoar


class Items(generics.ListCreateAPIView):

    if not Item.objects.count():
        povoar()


    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'album', 'duration', 'explicit']
    search_fields = ['name', 'album', 'duration', 'explicit']
    ordering_fields = ['name', 'album', 'duration', 'explicit']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
