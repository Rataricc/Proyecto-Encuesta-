from django.urls import path

from .views import *


urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),
	path('tablero/', tablero, name='tablero'),

]