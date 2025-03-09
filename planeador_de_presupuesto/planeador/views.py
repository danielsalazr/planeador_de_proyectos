from django.shortcuts import render, get_object_or_404
from django.db import connections, transaction
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.hashers import make_password
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status

import pandas as pd
from io import BytesIO
from rich.console import Console
from datetime import datetime

from .models import Cable, Presupuesto, EquipoRefrigeracion, GrupoCable

console = Console()

@api_view(('GET',))
def getInfoDatatable(request):
    cables = Cable.objects.all().values()
    return Response(cables, status=status.HTTP_200_OK)

@api_view(['POST'])
def crear_presupuesto(request):
    nombre = request.data.get('nombre')
    descripcion = request.data.get('descripcion')
    presupuesto = Presupuesto.objects.create(nombre=nombre, descripcion=descripcion)
    return Response({'id': presupuesto.id, 'nombre': presupuesto.nombre, 'descripcion': presupuesto.descripcion}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def crear_equipo(request, presupuesto_id):
    presupuesto = get_object_or_404(Presupuesto, id=presupuesto_id)
    nombre = request.data.get('nombre')
    descripcion = request.data.get('descripcion')
    equipo = EquipoRefrigeracion.objects.create(presupuesto=presupuesto, nombre=nombre, descripcion=descripcion)
    return Response({'id': equipo.id, 'nombre': equipo.nombre, 'descripcion': equipo.descripcion}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def crear_grupo(request, equipo_id):
    equipo = get_object_or_404(EquipoRefrigeracion, id=equipo_id)
    nombre = request.data.get('nombre')
    tipo = request.data.get('tipo')
    grupo = GrupoCable.objects.create(equipo=equipo, nombre=nombre, tipo=tipo)
    return Response({'id': grupo.id, 'nombre': grupo.nombre, 'tipo': grupo.tipo}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def crear_cable(request, grupo_id):
    grupo = get_object_or_404(GrupoCable, id=grupo_id)
    cable = Cable.objects.create(
        grupo=grupo,
        codigo_refrid_cable=request.data.get('codigo_refrid_cable'),
        descripcion_cable=request.data.get('descripcion_cable'),
        categoria_cable=request.data.get('categoria_cable'),
        aplicacion_cable=request.data.get('aplicacion_cable'),
        material_cable=request.data.get('material_cable'),
        temperatura_minima_operacion_cable=request.data.get('temperatura_minima_operacion_cable'),
        temperatura_maxima_operacion_cable=request.data.get('temperatura_maxima_operacion_cable'),
        consumo_nominal_cable=request.data.get('consumo_nominal_cable'),
        cantidad_hilos_cable=request.data.get('cantidad_hilos_cable'),
        calibre_cable=request.data.get('calibre_cable'),
        tension_nominal_cable=request.data.get('tension_nominal_cable'),
        apto_bandeja_cable=request.data.get('apto_bandeja_cable'),
        unidad_medida_cable=request.data.get('unidad_medida_cable'),
        libre_halogenos_cable=request.data.get('libre_halogenos_cable'),
        costo_cable=request.data.get('costo_cable'),
        moneda_cable=request.data.get('moneda_cable'),
        estado_cable=request.data.get('estado_cable'),
        fecha_actualizacion_cable=request.data.get('fecha_actualizacion_cable'),
        fuente_precio=request.data.get('fuente_precio')
    )
    return Response({'id': cable.id, 'codigo_refrid_cable': cable.codigo_refrid_cable}, status=status.HTTP_201_CREATED)

def calcular_caida_tension(cable):
    # Implementa la lógica para calcular la caída de tensión
    return 0.0

def calcular_factor_agrupamiento(cable):
    # Implementa la lógica para calcular el factor de agrupamiento
    return 1.0

@api_view(['GET'])
def obtener_detalles_cable(request, cable_id):
    cable = get_object_or_404(Cable, id=cable_id)
    caida_tension = calcular_caida_tension(cable)
    factor_agrupamiento = calcular_factor_agrupamiento(cable)
    return Response({
        'codigo_refrid_cable': cable.codigo_refrid_cable,
        'descripcion_cable': cable.descripcion_cable,
        'caida_tension': caida_tension,
        'factor_agrupamiento': factor_agrupamiento
    }, status=status.HTTP_200_OK)


