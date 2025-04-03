from django.db import models

# Create your models here.

# Tabla de cables
# codigo refrid
# nombre cable
# fabricante
# numero hilos
# aplicacion (instrumentacion, potencia, control, calentamiento ... etc)
# capacidad de corriente
# material de cable (cobre, aluminio)
# temperatura de operacion maxima
# temperatura de operacion minima
# Tension Nominal

class Planeacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nombre")
    numero = models.IntegerField(default=0, null=True, blank=True, verbose_name="Numericion")

    class Meta:
        verbose_name = 'Planeacion'
        verbose_name_plural = 'Planeacion'

    def __str__(self):
        return self.nombre