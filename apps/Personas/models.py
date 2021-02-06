from uuid import uuid4

from django.db import models

# Create your models here.
from apps.common.models import BaseModel


class Persona(BaseModel):
    class TiposIdentificacion(models.IntegerChoices):
        CEDULA = 0
        RUC = 1
        PASAPORTE = 2

    # Datos del Titular
    tipo_identificacion = models.PositiveSmallIntegerField(default=0, choices=TiposIdentificacion.choices)
    identificacion = models.CharField(max_length=30, unique=True)

    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True, default=None)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True, default=None)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    # Informacion de contactos
    telefono = models.CharField(max_length=30, null=True, blank=True)
    extension = models.CharField(max_length=30, null=True, blank=True)
    celulares = models.ManyToManyField('Contactos', blank=True)
    correos = models.ManyToManyField('Contactos', blank=True)
    canal_preferido = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'Personas'


class Contactos(BaseModel):
    contacto = models.CharField(max_length=30)
    tipo = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'Contactos'


class Provincia(BaseModel):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150, default=uuid4)

    class Meta:
        db_table = 'Provincias'


class Canton(BaseModel):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150, default=uuid4)
    provincia = models.ForeignKey(Provincia, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Cantones'
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantones'


class Parroquia(BaseModel):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150)
    canton = models.ForeignKey(Canton, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Parroquias'


class Calle(BaseModel):
    class TiposCalle(models.IntegerChoices):
        PRINCIPAL = 0
        SECUNDARIA = 1

    calle = models.TextField()
    tipo = models.PositiveSmallIntegerField(default=0, choices=TiposCalle.choices)

    class Meta:
        db_table = 'Calles'


class Barrio(BaseModel):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, default=uuid4)

    class Meta:
        db_table = 'Barrios'


class Cliente(BaseModel):
    class TiposPersona(models.IntegerChoices):
        NATURAL = 0
        JURIDICA = 1

    class TipoInmueble(models.IntegerChoices):
        PROPIETARIO = 0
        APODERADO = 1

    class DatosConyugue(models.IntegerChoices):
        CEDULA = 0
        PASAPORTE = 1
        SIN_CONYUGE = 2

    class TiposUsoMedidor(models.IntegerChoices):
        PROPIETARIO = 0
        ARRENDATARIO = 1
        APODERADO = 2
        FAMILIAR = 3
        OTRO = 4

    class TipoPropiedad(models.IntegerChoices):
        CASA = 0
        DEPARTAMENTO = 1

    class TipoUsoEnergia(models.IntegerChoices):
        RESIDENCIAL = 0
        COMERCIAL = 1
        INDUSTRIAL = 2
        OTRO = 3

    class ProgramasDeCoccionEficiente(models.IntegerChoices):
        COCINA = 0
        DUCHA = 1
        AMBOS = 2
        NINGUNO = 3

    class TiposConsumoEnergia(models.IntegerChoices):
        PRIVADO = 0
        PUBLICO = 1

    persona = models.ForeignKey(Persona, unique=True, on_delete=models.RESTRICT)
    tipo_persona = models.PositiveSmallIntegerField(default=0, choices=TiposPersona.choices)
    inmueble = models.PositiveSmallIntegerField(default=0, choices=TipoInmueble.choices)

    # Datos del Conyuge
    conyuge = models.PositiveSmallIntegerField(default=2, choices=DatosConyugue.choices)
    info_conyuge = models.JSONField(blank=True, null=True)

    # Persona / Empresa Que usa el Medidor
    tipo_uso_medidor = models.PositiveSmallIntegerField(default=0, choices=TiposUsoMedidor.choices)

    # Direccion Completa Punto Suministro
    provincia = models.ForeignKey(Provincia, on_delete=models.RESTRICT)
    canton = models.ForeignKey(Canton, on_delete=models.RESTRICT)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.RESTRICT)

    calle_principal = models.ForeignKey(Calle, on_delete=models.RESTRICT)
    calle_secundaria = models.ForeignKey(Calle, on_delete=models.RESTRICT)

    sector_direccion = models.TextField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=30)

    tipo_propiedad = models.PositiveSmallIntegerField(default=0, choices=TipoPropiedad.choices)
    numero_casa = models.CharField(max_length=30)
    numero_piso = models.PositiveSmallIntegerField(default=1)
    barrio = models.ForeignKey(Barrio, on_delete=models.RESTRICT)

    # Telefonos y Correo Electronico(Ya esta en el modelo de Persona)

    # Uso de energia
    producto_tarifa = models.CharField(max_length=30)  # codigo unico de la empresa electrica
    # (tipo_uso_energia) Cuando seleccione otro se debe especificar
    tipo_uso_energia = models.PositiveSmallIntegerField(default=0, choices=TipoUsoEnergia.choices)
    especificacion_otro_uso_energia = models.TextField(blank=True, null=True)
    especificacion_uso = models.TextField()
    pec = models.PositiveSmallIntegerField(default=0, choices=ProgramasDeCoccionEficiente.choices)
    tipo_consumo = models.PositiveSmallIntegerField(default=0, choices=TiposConsumoEnergia.choices)

    # Subsidios
    # verificacion_supervivencia = models.TextField() campo eliminado

    class Meta:
        db_table = 'Clientes'
