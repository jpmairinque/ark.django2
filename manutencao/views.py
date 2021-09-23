from django.shortcuts import render
from rest_framework import viewsets, generics
import requests
from .models import Chamado, Company, Equipment
from .serializer import CompanySerializer, EquipmentSerializer, CompanyEquipmentsSerializer, ChamadoSerializer, EquipmentChamadosSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
class CompanyEquipmentsViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Equipment.objects.filter(proprietario=self.kwargs['pk'])
        return queryset
    
    serializer_class = CompanyEquipmentsSerializer


class EquipmentChamadosViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Chamado.objects.filter(equipamento_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = EquipmentChamadosSerializer

