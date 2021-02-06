from django.db import models
from django.utils import dateparse


class BaseModel(models.Model):
    class AuthEstados(models.IntegerChoices):
        INACTIVO = 0
        ACTIVO = 1

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_estado = models.PositiveSmallIntegerField(default=1, choices=AuthEstados.choices)

    class Meta:
        abstract = True

    def __to_json__(self):
        obj_json = self.__dict__
        obj_json['created_at'] = self.created_at.isoformat()
        obj_json['updated_at'] = self.updated_at.isoformat()
        obj_json.pop('_state')
        return obj_json
