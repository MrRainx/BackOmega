import graphene

from apps.Censos.models import PeriodoActializacion, FormularioActualizacion
from apps.Censos.types import PeriodoActualizacionType, FormularioActualizacionType


class CensoQueries(graphene.ObjectType):
    periodos = graphene.List(PeriodoActualizacionType)

    formulario = graphene.Field(FormularioActualizacionType)

    def resolve_periodos(self, info):
        return PeriodoActializacion.objects.all()

    def resolve_formulario(self, info):
        return FormularioActualizacion.objects.first()
