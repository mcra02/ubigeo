# Django
from django.contrib import admin
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# ViewSets
from api.views import (
    DepartamentoViewSet,
    ProvinciaViewSet,
    DistritoViewSet
)
from api.views import FileViewSet

router = DefaultRouter()
router.register(r'departamento', DepartamentoViewSet, basename='departamento')
router.register(r'provincia', ProvinciaViewSet, basename='provincia')
router.register(r'distrito', DistritoViewSet, basename='distrito')

router.register(r'file', FileViewSet, basename='file')

urlpatterns = [
    path('', include(router.urls))
]
