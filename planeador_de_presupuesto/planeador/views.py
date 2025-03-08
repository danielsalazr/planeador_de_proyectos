from django.shortcuts import render
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
# Create your views here.


import pandas as pd
from io import BytesIO
# import django_excel as excel
# from pyexcel_xlsx  import save_data
from rich.console import Console
from datetime import datetime

console = Console()



def templateArticulos(request):

    context = {}
    
    return render(request, "planeador/index.html", context)
@api_view(('GET',))
def getInfoDatatable(request):

    query ="""
        SELECT
            CODIGO,
            REFRID,
            DESCRIPCION,
            `UM.`,
            COSTO,
            COSTO2,
            COSTO3,
            L,
            G,
            E,
            MONEDA,
            `USD COMERCIALIZ`,
            `USD ENSAMBLE`,
            `USD FABRICACION`,
            `COP COMERCIALIZACION`,
            `COP ENSAMBLE`,
            `COP FABRICACION`,
            ESTADO,
            PARETO,
            `FECHA DE ACTUALIZACIÓN`,
            `FUENTE DEL PRECIO`
        FROM rdc.articulos;
        ;
    """

    with connections['default'].cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    # users = Colaboradores.objects.all().values()

    # console.log(users)

    return Response(results,status=status.HTTP_200_OK)