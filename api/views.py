from django.shortcuts import render

# Create your views here.

# File
import pickle
from pathlib import Path
import json

# Rest Framework
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

# Models
from api.models import (
    Departamento,
    Provincia,
    Distrito
)

# Serializers
from api.serializers import (
    DepartamentoSerializer,
    ProvinciaSerializer,
    DistritoSerializer
)
from api.serializers import FileSerializer

# Script
from api.script_data import ScriptExcel

class DepartamentoViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class ProvinciaViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class DistritoViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class FileViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = FileSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        array_index = request.data['encabezado'].split(',')
        root = Path(".")
        xls_path = root / "file" /  str(request.data['file_xls'])
        with open(xls_path, 'wb') as output:
            pickle.dump(request.data['file_xls'], output, pickle.HIGHEST_PROTOCOL)
        data = ScriptExcel.extractData(self, xls_path, request.data['key'], array_index)
        elements = ScriptExcel.mapData(self, json.loads(data))
        res = ScriptExcel.inserData(self, elements)
        return Response(res)