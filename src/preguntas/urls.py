from django.urls import path
from .       	 import views

app_name = "preguntas"

urlpatterns = [
	path('Preguntaree/', views.preguntar, name="preguntar"),
	path('jugar/', views.jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='resultado'),

]