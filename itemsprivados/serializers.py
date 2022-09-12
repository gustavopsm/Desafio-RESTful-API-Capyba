from rest_framework import serializers
from .models import ItemPrivado

class ItemPrivadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPrivado
        fields = ['name', 'album', 'duration', 'explicit']