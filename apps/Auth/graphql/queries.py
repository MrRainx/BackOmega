import graphene
import graphene_django
from django.core.handlers.wsgi import WSGIRequest
from graphql import ResolveInfo

from apps.Auth.graphql.types import PermisoType, GrupoType, UsuarioType
from apps.Auth.models import Permiso, Rol, Usuario


class AuthQueries(graphene.ObjectType):
    permisos = graphene.List(PermisoType)
    permiso = graphene.Field(PermisoType, id=graphene.ID(required=True))

    grupos = graphene.List(GrupoType)
    grupo = graphene.Field(GrupoType, id=graphene.ID(required=True))

    usuarios = graphene_django.DjangoListField(UsuarioType)
    usuario = graphene.Field(UsuarioType, id=graphene.ID(required=True))
    me = graphene.Field(UsuarioType)

    def resolve_permiso(self, info, id):
        return Permiso.objects.filter(id=id).first()

    def resolve_permisos(self, info):
        return Permiso.objects.all().order_by('nombre')

    def resolve_grupo(self, info, id):
        return Rol.objects.filter(id=id).first()

    def resolve_grupos(self, info):
        return Rol.objects.all()

    def resolve_usuario(self, info, id):
        return Usuario.objects.filter(id=id).first()

    def resolve_usuarios(self, info):
        return Usuario.objects.all()

    def resolve_me(self, info: ResolveInfo):
        context: WSGIRequest = info.context
        if context.user.pk:
            return context.user

        return None
