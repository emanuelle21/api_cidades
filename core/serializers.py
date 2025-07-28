

from rest_framework import serializers
from .models import Estado, Cidade

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    # Mostra os dados do estado completo
    estado = EstadoSerializer(read_only=True)
    # Permite enviar só o ID do estado ao criar cidade
    estado_id = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all(), source='estado')

    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'estado_id']
