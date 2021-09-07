from django.urls import path

from .views import *

app_name = 'quiz'
urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('Usuario/', HomeUsuario, name='HomeUsuario'),  #encuentren a qué esta linkeado esto y borrenlo, 
	#cambienlo por solamente el ('' inicio) porq es muy redundante


	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),
	path('tablero/', tablero, name='tablero'),

	
	path('jugar/', jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),

]