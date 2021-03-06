import graphene
from graphene_django import DjangoObjectType

from apps.Auth.models import Permiso, Rol, Usuario


class PermisoType(DjangoObjectType):
    class Meta:
        model = Permiso


class GrupoType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    numero_permisos = graphene.Int()

    class Meta:
        model = Rol

    def resolve_permisos_disponibles(self: Rol, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))

    def resolve_numero_permisos(self: Rol, info):
        return self.permisos.get_queryset().count()


class UsuarioType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    grupos_disponibles = graphene.List(GrupoType)
    numero_permisos = graphene.Int()
    numero_grupos = graphene.Int()

    class Meta:
        model = Usuario

    def resolve_permisos_disponibles(self: Usuario, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))

    def resolve_grupos_disponibles(self: Usuario, info):
        return Rol.objects.exclude(id__in=self.grupos.get_queryset().values_list('id'))

    def resolve_numero_permisos(self: Usuario, info):
        return self.permisos.get_queryset().count()

    def resolve_numero_grupos(self: Usuario, info):
        return self.grupos.get_queryset().count()
