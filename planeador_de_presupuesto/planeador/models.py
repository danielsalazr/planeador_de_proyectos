from django.db import models

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class EquipoRefrigeracion(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, related_name='equipos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class GrupoCable(models.Model):
    equipo = models.ForeignKey(EquipoRefrigeracion, related_name='grupos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('potencia', 'Potencia'), ('control', 'Control')])

    def __str__(self):
        return self.nombre

class Cable(models.Model):
    grupo = models.ForeignKey(GrupoCable, related_name='cables', on_delete=models.CASCADE)
    codigo_refrid_cable = models.CharField(max_length=20, null=True, blank=True)
    descripcion_cable = models.CharField(max_length=80, null=True, blank=True)
    categoria_cable = models.CharField(max_length=20, null=True, blank=True)
    aplicacion_cable = models.CharField(max_length=20, null=True, blank=True)
    material_cable = models.CharField(max_length=20, null=True, blank=True)
    temperatura_minima_operacion_cable = models.CharField(max_length=20, null=True, blank=True)
    temperatura_maxima_operacion_cable = models.CharField(max_length=20, null=True, blank=True)
    consumo_nominal_cable = models.CharField(max_length=20, null=True, blank=True)
    cantidad_hilos_cable = models.IntegerField(null=True, blank=True)
    calibre_cable = models.CharField(max_length=10, null=True, blank=True)
    tension_nominal_cable = models.CharField(max_length=20, null=True, blank=True)
    apto_bandeja_cable = models.BooleanField(null=True, blank=True)
    unidad_medida_cable = models.CharField(max_length=20, null=True, blank=True)
    libre_halogenos_cable = models.BooleanField(null=True, blank=True)
    costo_cable = models.CharField(max_length=20, null=True, blank=True)
    moneda_cable = models.CharField(max_length=20, null=True, blank=True)
    estado_cable = models.CharField(max_length=20, null=True, blank=True)
    fecha_actualizacion_cable = models.DateField(null=True, blank=True)
    fuente_precio = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.codigo_refrid_cable


