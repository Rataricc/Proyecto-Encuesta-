from django.db import models

import datetime

from django.utils import timezone 
#estamos haciendo una herencia, pues pregunta hereda de models.model
class  Preguntas(models.Model): 
	texto_Preguntas = models.CharField(max_length = 255 )
	fecha_publicacion = models.DateTimeField('Fecha de publicacion')
	class Meta():
		db_table = 'preguntas'
	def __str__ (self):
		return self.texto_Preguntas
	def fecha_de_carga (self):
		ahora = timezone.now()    #ese ahora menos datetime va a ser menor q la variable fecha de pub
		return ahora-datetime.timedelta(days = 1 )<= self.fecha_publicacion<= ahora 



	
	
