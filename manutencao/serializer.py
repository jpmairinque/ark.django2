from django.db.models import fields
from rest_framework import serializers

from .models import Company, Equipment, Chamado

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'

class CompanyEquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentChamadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = '__all__'