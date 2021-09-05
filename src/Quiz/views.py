from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from .forms import RegistroFormulario, UsuarioLoginFormulario

from .models import QuizUsuario, Pregunta, PreguntasRespondidas


def inicio(request):
	return render(request, 'inicio.html')


def HomeUsuario(request):

	return render(request, 'Usuario/home.html')


def tablero(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {

		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}

	return render(request, 'play/tablero.html', context)

def jugar(request):

	QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('resultado', pregunta_respondida.pk)

	else:
		pregunta = QuizUser.obtener_nuevas_preguntas()
		if pregunta is not None:
			QuizUser.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, 'play/jugar.html', context)
#####################
def crear_intentos(self, pregunta):
    intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
    intento.save()

def obtener_nuevas_preguntas(self):
    respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
    preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
    if not preguntas_restantes.exists():
      return None
    return random.choice(preguntas_restantes)

def validar_intentos(self, pregunta_respondida, respuesta_selecionada):

    if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
      return 


    pregunta_respondida.respuesta_selecionada = respuesta_selecionada
    if respuesta_selecionada.correcta is True:
      pregunta_respondida.correcta = True
      pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
    pregunta_respondida.save()

####################
def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'play/resultados.html', context)

def loginView(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('inicio')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, 'Usuario/login.html', context)

def registro(request):

	titulo = 'Crear una Cuenta'
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistroFormulario()

	context = {

		'form':form,
		'titulo': titulo

	}

	return render(request, 'Usuario/registro.html', context)


def logout_vista(request):
	logout(request)
	return redirect('/')

