from django.db                  import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
	class Meta: 
		db_table = 'user' 
"""
class QuizUsuario(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name = 'Puntaje Tota', default = 0 , )"""