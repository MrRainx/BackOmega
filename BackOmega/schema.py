import graphene
from graphene_django.debug import DjangoDebug

from apps.Auth.graphql.queries import AuthQueries
from apps.Auth.schema import AuthMutations
from apps.Censos.queries import CensoQueries
from apps.Utils.queries import UtilsQueries
from apps.Utils.schema import UtilsMutations


class RootQueries(
    AuthQueries,
    # MeQuery,
    CensoQueries,
    UtilsQueries,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name='_debug')

    class Meta:
        description = 'Consultas disponibles'


class RootMutation(
    AuthMutations,
    UtilsMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    # types=[ImagenType],
    query=RootQueries,
    mutation=RootMutation,
)
