# Rest Framework
from rest_framework import serializers

# Models
from api.models import (
    Departamento,
    Provincia,
    Distrito
)

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provincia
        fields = '__all__'

class DistritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distrito
        fields = '__all__'

class FileSerializer(serializers.Serializer):

    file_xls = serializers.FileField()

    key = serializers.CharField(
        allow_null=False,
        allow_blank=False,
        max_length=100
    )
    
    encabezado = serializers.ListField(
        child = serializers.CharField(
            max_length=100,
            allow_null=False,
            allow_blank=False
        )
    )