from django.shortcuts import render

def inicio(request):
	return render(request,'index.html')

"""
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
	"""

def principal(request):
	template_name = "principal.html"
	ctx = {
		
	}
	return render(request, template_name, ctx)

def Logeo(request):
	template_name = "loginvista.html"
	return render(request, template_name)

def registro(request):
	template_name = "registrarvista.html"
	return render(request, template_name)