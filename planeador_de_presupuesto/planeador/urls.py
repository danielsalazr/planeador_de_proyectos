from django.urls import path
from . import views

urlpatterns = [
    path('getInfoDatatable/', views.getInfoDatatable, name="getInfoDatatable"),
    path('presupuestos/', views.crear_presupuesto, name='crear_presupuesto'),
    path('presupuestos/<int:presupuesto_id>/equipos/', views.crear_equipo, name='crear_equipo'),
    path('equipos/<int:equipo_id>/grupos/', views.crear_grupo, name='crear_grupo'),
    path('grupos/<int:grupo_id>/cables/', views.crear_cable, name='crear_cable'),
]