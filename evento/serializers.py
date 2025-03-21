from .models import Event
from rest_framework import serializers #pip install djangorestframework
# serializer pega os dados que chegam em forma de objeto e converte eles para json 


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' # para pegar todos os dados