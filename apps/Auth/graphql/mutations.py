from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from apps.Auth.models import Permiso, Rol, Usuario


class CreatePermisoMutation(DjangoCreateMutation):
    class Meta:
        model = Permiso


class UpdatePermisoMutation(DjangoUpdateMutation):
    class Meta:
        model = Permiso


class DeletePermisoMutation(DjangoDeleteMutation):
    class Meta:
        model = Permiso


class CreateGrupoMutation(DjangoCreateMutation):
    class Meta:
        model = Rol


class UpdateGrupoMutation(DjangoUpdateMutation):
    class Meta:
        model = Rol


class DeleteGrupoMutation(DjangoDeleteMutation):
    class Meta:
        model = Rol


class CreateUsuarioMutation(DjangoCreateMutation):
    class Meta:
        model = Usuario
        optional_fields = ('password',)

    @classmethod
    def after_mutate(cls, root, info, obj: Usuario, return_data):
        obj.password = '1234ABC'
        obj.set_password(obj.password)
        obj.save()
        return super().after_mutate(root, info, obj, return_data)


class UpdateUsuarioMutation(DjangoUpdateMutation):
    class Meta:
        model = Usuario
        optional_fields = ('password',)


class DeleteUsuarioMutation(DjangoDeleteMutation):
    class Meta:
        model = Usuario
