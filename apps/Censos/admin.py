from django.contrib import admin
from django.db import models
from jsoneditor.forms import JSONEditor

from apps.Censos.models import PeriodoActializacion, FormularioActualizacion


# Register your models here.


@admin.register(PeriodoActializacion)
class PeriodoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'auth_estado')
    list_display_links = ('id', 'nombre',)
    search_fields = ('id', 'nombre', 'fecha_inicio', 'fecha_fin', 'estado', 'auth_estado')

    fieldsets = [
        ('Información', {
            'fields': [
                ('nombre',),
                ('fecha_inicio', 'fecha_fin'),
            ]
        }),
        ('Estados', {
            'fields': [
                ('estado', 'auth_estado')
            ]
        })
    ]
    list_filter = ['estado', 'auth_estado']


def dynamic_schema(widget):
    return {
        'type': 'array',
        'title': 'tags',
        'items': {
            'type': 'string',
            'enum': ['PRUEBA'],
        }
    }


@admin.register(FormularioActualizacion)
class FormularioActualizacionAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'get_periodo', 'auth_estado')
    list_display_links = ('id', 'get_periodo',)
    search_fields = ('id', 'periodo', 'auth_estado')

    fieldsets = [
        ('Información', {
            'fields': [
                ('periodo',),
            ]
        }),
        ('Secciones', {
            'fields': [
                ('secciones',),
            ]
        }),
        ('Campos', {
            'fields': [
                ('fields',),
            ]
        }),
        ('Estados', {
            'fields': [
                ('auth_estado',)
            ]
        })
    ]
    list_filter = ['auth_estado', ]
    autocomplete_fields = ('periodo',)

    def get_periodo(self, obj: FormularioActualizacion):
        return f'{obj.periodo.nombre}'

    get_periodo.short_description = 'Periodo'
    get_periodo.admin_order_field = 'periodo'

    formfield_overrides = {
        # models.CharField: {'widget': Textarea(attrs={'size': '20'})},

        models.JSONField: {
            'widget': JSONEditor

        }

    }

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     widget = JSONEditorWidget(dynamic_schema, False)
    #     form = super().get_form(
    #         request,
    #         obj,
    #         widgets={
    #             'fields': widget
    #         },
    #         **kwargs)
    #     return form
