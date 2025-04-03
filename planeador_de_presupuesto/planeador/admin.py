from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Planeacion)
class ComisionesColaboradoresAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'numero',
    )