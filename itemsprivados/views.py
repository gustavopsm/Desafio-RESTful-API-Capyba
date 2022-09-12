from .models import ItemPrivado
from .serializers import ItemPrivadoSerializer
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from .povoar import povoar

class ItemsPrivados(generics.ListCreateAPIView):

    if not ItemPrivado.objects.count():
        povoar()
        
    queryset = ItemPrivado.objects.all()
    serializer_class = ItemPrivadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'album', 'duration', 'explicit']
    search_fields = ['name', 'album', 'duration', 'explicit']
    ordering_fields = ['name', 'album', 'duration', 'explicit']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.verificado:
            return super().dispatch(*args, **kwargs)