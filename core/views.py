from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Estado, Cidade
from .serializers import EstadoSerializer, CidadeSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
