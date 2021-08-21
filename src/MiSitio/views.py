from django.shortcuts import render

def inicio(request):
	template_name = "inicio.html"

	lista_de_alumnos = [
		'Usuario 3',
		'Usuario 4'
	]

	ctx = {
		'username': 'Lautaro Rataric',
		'lista': lista_de_alumnos
	}
	return render(request, template_name, ctx)

def principal(request):
	template_name = "principal.html"
	ctx = {
		
	}
	return render(request, template_name, ctx)
