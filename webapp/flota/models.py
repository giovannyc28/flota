from django.db import models

# Create your models here.
class Propietarios(models.Model):
	TIPODOC = (
		('CC', 'Cedula de Ciudadania'),
		('NIT', 'Nit'),
		('CE', 'Cedula de Extranjeria'),
	)
	nuip = models.CharField(max_length=15, primary_key=True)
	tipodoc = models.CharField(max_length=3, choices=TIPODOC)
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	email = models.CharField(max_length=60)

	def __str__(self):
		return self.nombres + ' ' + self.apellidos


class Vehiculos(models.Model):
	TIPOVEH = (
		('A', 'Automovil - Camioneta'),
		('C', 'Camion'),
		('M', 'Moto'),
		('P', 'De Carga'),
		('Q', 'Cuatrimoto'),
		('H', 'Ciclo Motor'),
	)
	TIPOSERV = (
		('R', 'Particular'),
		('P', 'Publico'),
		('O', 'Oficial'),
	)
	placa = models.CharField(max_length=10, primary_key=True)
	tipo_vehiculo = models.CharField(max_length=1, choices=TIPOVEH)
	marca = models.CharField(max_length=30)
	modelo = models.IntegerField(default=0)
	cilindraje = models.IntegerField(default=0)
	tipo_servicio = models.CharField(max_length=1, choices=TIPOSERV)
	propietario = models.ForeignKey(Propietarios)