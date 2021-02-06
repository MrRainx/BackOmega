from django.db import models

# Create your models here.
from apps.common.models import BaseModel


class PeriodoActializacion(BaseModel):
    class EstadosPeriodo(models.IntegerChoices):
        CERRADO = 0
        ABIERTO = 1

    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.PositiveSmallIntegerField(default=1, choices=EstadosPeriodo.choices)

    class Meta:
        db_table = 'PeriodosDeActualizacion'
        verbose_name = 'Periodo de Actualización'
        verbose_name_plural = 'Periodos de Actualización'


class Censo(BaseModel):
    class TiposIdentificacion(models.IntegerChoices):
        CEDULA = 0
        RUC = 1
        PASAPORTE = 2

    class EstadosCenso(models.IntegerChoices):
        CENSO_INCOMPLETO = 0
        CENSO_COMPLETO = 1

    periodo = models.ForeignKey(PeriodoActializacion, on_delete=models.RESTRICT)
    estado_censo = models.PositiveSmallIntegerField(default=0, choices=EstadosCenso.choices)

    # Datos del Titular
    tipo_identificacion = models.PositiveSmallIntegerField(default=0, choices=TiposIdentificacion.choices)
    identificacion = models.CharField(max_length=30, unique=True)

    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True, default=None)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    fields = models.JSONField()

    class Meta:
        db_table = 'Censos'
        unique_together = ('periodo', 'identificacion',)


class FormularioActualizacion(BaseModel):
    periodo = models.OneToOneField(PeriodoActializacion, on_delete=models.RESTRICT)
    fields = models.JSONField()
    secciones = models.JSONField()

    class Meta:
        db_table = 'FormulariosActualizacion'
        verbose_name = 'Formulario de actualización'
        verbose_name_plural = 'Formularios de actualización'
