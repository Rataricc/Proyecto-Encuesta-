from django.db import models

# Create your models here.

class Pregunta(models.Model): 
	texto = models.TextField(verbose_name='Texto de la pregunta')

	class Meta: 
		db_table= 'pregunta'

	def __str__(self): 
		return self.texto

class Opciones(models.Model): 
	pregunta = models.ForeignKey(Pregunta, related_name='pregunta', on_delete=models.CASCADE)
	es_correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?',default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')

	class Meta: 
		db_table= 'opciones'

	def __str__(self): 
		return self.texto

