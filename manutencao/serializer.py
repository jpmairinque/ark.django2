from django.db.models import fields
from rest_framework import serializers

from .models import Company, Equipment

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'