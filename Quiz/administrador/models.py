import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Pregunta(models.Model):
	pregunta_text = models.TextField(verbose_name='Texto de la pregunta')
	fecha_publ = models.DateTimeField('Fecha de publicacion')

	class Meta:
		db_table = 'pregunta'

	def __str__(self):
		return self.pregunta_text

	def publicacion_reciente(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1)<= self.fecha_publ <= now



class Opcion(models.Model):
	cuestion = models.ForeignKey(Pregunta, related_name = 'preguntas', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name= 'es esta la pregunta correcta?',default = False, null = False) 
	 #verbose_name hace que la base de datos muestre esto con ese nombre referencial 
	opcion_text = models.TextField(verbose_name='Texto de la respuesta')
	votos = models.IntegerField(default=0)

	class Meta:
		db_table = 'opcion'

	def __str__(self):
		return self.opcion_text
#nos permite observar el texto de la respuesta

"""
class Usuario(models.Model):
	nombre = models.CharField(max_length=150)
	contraseña = models.CharField(max_length=50)
	es_admin = models.BooleanField(default=False)

	class Meta:
		db_table = 'Usuario'

	def __str__(self):
		return self.Usuario_text

class Participaciones(models.Model):
	id_usuario = models.ForeignKey(Usuario)	
	id_juego = models.ForeignKey(Juego)

class Juego(models.Model):
	fecha  = models.DateField('Fecha de publicacion')
	puntuacion = models.IntegerField(default=0)

class Seleccion(models.Model):-
	id_juego = models.ForeignKey(Juego)
	id_opcion = models.ForeignKey(Opcion)

class Opcion(models.Model):
	id_pregunta= models.ForeignKey(Pregunta)

class Pregunta (models.Model):
	texto= models.CharField(max_length=150)
	valor = models.BooleanField(default=false)
"""