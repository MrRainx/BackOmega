import graphene
import graphene_django
from graphene.types.generic import GenericScalar

from apps.Censos.models import PeriodoActializacion, FormularioActualizacion, Censo


class PeriodoActualizacionType(graphene_django.DjangoObjectType):
    class Meta:
        model = PeriodoActializacion


class CensoType(graphene_django.DjangoObjectType):
    class Meta:
        model = Censo


class FormularioActualizacionType(graphene_django.DjangoObjectType):
    secciones = graphene.types.generic.GenericScalar()

    class Meta:
        model = FormularioActualizacion
