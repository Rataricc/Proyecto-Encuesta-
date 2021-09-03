from django.shortcuts 				import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins 	import LoginRequiredMixin
from django.views.generic 			import ListView
from .models 						import User
from .forms 						import RegistroFormulario , UsuarioLoginFormulario
from django.contrib.auth 			import authenticate, login 
from django.contrib.auth.models 	import User
 


# Create your views here.
"""
def listar_usuarios(request): 
	template_name = "user/listarusuarios.html"
	lista_de_usuarios = User.objects.all()
	ctx = {
		'usuarios' : lista_de_usuarios
	}
	return render(request, template_name, ctx)"""
										
def inicio(request): 
	template_name = "inicio.html"
	ctx = {

	}
	return render(request, template_name, ctx)
										
"""

def nuevo_amigo(request): 
	template_name = "user/nuevo.html"
	ctx = {
		'form': AmigoForm()
	}
	return render(request, template_name, ctx)

class Listar(LoginRequiredMixin, ListView): 
	template_name = "user/listarusuarios.html" # Seguir despues, tiene un error... video Vistas basadas en funciones
													# y en clases--- 10: 00
	model = user
	
	context_object_name = 'user'

	def get_queryset(self): 
		if self.request.user.is_superuser: 
			return User.objects.all()
		

		return User.objects.filter(nombre="Belen")"""
#################################################
def registro(request):
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user:login')
	else :
			form = RegistroFormulario()
	ctx = {

	'form': form,
	

	}
	return render(request,'register.html',ctx) 

def loginView(request):
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username = username, password = password)
		login(request, usuario)
		return redirect('/')
	ctx = {

	'form':form,

	}
	return render(request,'login.html', ctx)
#################################################