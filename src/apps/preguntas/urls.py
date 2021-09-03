from django.urls import path
from .           import views

app_name = "preguntas"

urlpatterns = [
	path('Preguntaree/', views.preguntar, name="preguntar"),
]