from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from apps.common.models import BaseModel


# Create your models here.


# from apps.Personas.models import Persona


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, password, **extra_fields)


class Permiso(BaseModel):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Permiso'


class Rol(BaseModel):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    permisos = models.ManyToManyField(Permiso)

    class Meta:
        db_table = 'Roles'


class Usuario(PermissionsMixin, AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    roles = models.ManyToManyField(Rol, blank=True)
    permisos = models.ManyToManyField(Permiso, blank=True)
    first_name = models.CharField(default="NO REGISTRA", null=True, max_length=150)
    last_name = models.CharField(default="NO REGISTRA", null=True, max_length=150)

    # persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Usuarios'


class Perfil(BaseModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    foto = models.URLField(null=True, blank=True)
    nombres = models.CharField(max_length=150, blank=True, null=True)
    apellidos = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'Perfiles'
