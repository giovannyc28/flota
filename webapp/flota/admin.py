from django.contrib import admin

from .models import Vehiculos, Propietarios

class VehiculosInline(admin.TabularInline):
    model = Vehiculos
    extra = 0
    fields = ["placa", "tipo_vehiculo", "marca", "modelo", "cilindraje", "tipo_servicio"]

class PropietariosAdmin(admin.ModelAdmin):
    inlines = [VehiculosInline]
    list_display = ('nuip', 'nombres', 'apellidos')
    search_fields = ['nuip', 'nombres', 'apellidos']

class VehiculosAdmin(admin.ModelAdmin):
    list_display = ('placa', 'tipo_vehiculo', 'marca', 'modelo', 'cilindraje', 'tipo_servicio', 'propietario')
    search_fields = ['placa', 'marca', 'propietario__nombres', 'propietario__apellidos']
    list_filter = ['tipo_vehiculo', 'marca', 'modelo']


admin.site.register(Propietarios, PropietariosAdmin)
admin.site.register(Vehiculos, VehiculosAdmin)
