from django.shortcuts 	  import render
from django.views.generic import ListView, CreateView
from django.urls          import reverse_lazy
from .forms               import PreguntasForm, PreguntasForm2

# Create your views here.

"""
def preguntar2(request): 
	template_name = "preguntas/jugar.html"
	ctx = {}

	if request.method == "POST":
		respuestas_marcadas = request.POST.getlist('respuestas')

	ctx["form"] = PreguntasForm(pregunta="¿Resitencia es conocida como?",respuestas=[(1, "La Ciudad de las esculturas"),(2, "Ciudad Museo"), (3, "Ciudad Capital")])

	return render(request, template_name, ctx)
"""
class Preg: 
	def __init__(self, descripcion, lista_respuestas): 
		self.descripcion = descripcion
		self.lista_respuestas = lista_respuestas

	def __str__(self): 
		return self.descripcion

class Resp: 
	def __init__(self,descripcion, es_correcta,id_resp): 
		self.descripcion = descripcion
		self.es_correcta = es_correcta
		self.id_resp = id_resp


def preguntar(request): 
	template_name = "preguntas/jugar.html"
	ctx = {}

	if request.method == "POST": 
		respuestas_marcadas = request.POST.getlist('respuestas')
		pass


	r1 = Resp(descripcion="200", es_correcta= False, id_resp=1)
	r2 = Resp(descripcion="700", es_correcta= False, id_resp=2)
	r3 = Resp(descripcion="600", es_correcta= True, id_resp=3)
	x =[r1, r2, r3]

	p1 = Preg(descripcion="¿Cuantas esculturas hay en Resistencia?", lista_respuestas= x)


	r4 = Resp(descripcion="Litoral Chaqueño, centro Chaqueño e impenetrable Chaqueño", es_correcta= True, id_resp=1)
	r5 = Resp(descripcion="Litoral Chaqueño e impenetrable Chaqueño", es_correcta= False, id_resp=2)
	r6 = Resp(descripcion="Chaco Boreal y Chaco Austral", es_correcta= False, id_resp=3)
	x = [r4, r5, r6]

	p2 = Preg(descripcion="¿En que sectores se divide geograficamente la provincia del Chaco", lista_respuestas= x)

	r7 = Resp(descripcion="Maipu", es_correcta= False, id_resp=1)
	r8 = Resp(descripcion="Bermejo", es_correcta= False, id_resp=2)
	r9 = Resp(descripcion= "12 de Octubre", es_correcta= True, id_resp=3)
	x = [r7, r8, r9]

	p3 = Preg(descripcion="Campo del Cielo: Patrimonio Cultural y Turistico del Chaco, ¿Donde se ubica?", lista_respuestas= x)

	r10 = Resp(descripcion="Pilcomayo", es_correcta= False, id_resp=1)
	r11 = Resp(descripcion="Parana", es_correcta= False, id_resp=2)
	r12 = Resp(descripcion= "Bermejo", es_correcta= True, id_resp=3)
	x = [r10, r11, r12]

	p4 = Preg(descripcion="Al norte el limite natural establecido entre la Provincia de Chaco y Formosa es:", lista_respuestas= x)

	r13 = Resp(descripcion="Paralelo 28", es_correcta= True, id_resp=1)
	r14 = Resp(descripcion="Paralelo 30", es_correcta= False, id_resp=2)
	r15 = Resp(descripcion= "Paralelo 29", es_correcta= False, id_resp=3)
	x = [r13, r14, r15]

	p5 = Preg(descripcion= "Al sur el limite establecido entre la Provincia del Chaco y Santa Fe es:", lista_respuestas= x)

	r16 = Resp(descripcion="Puerto de Barranqueres con Formosa", es_correcta= False, id_resp=1)
	r17 = Resp(descripcion="Puerto de Barranquras con Salta", es_correcta= True, id_resp=2)
	r18 = Resp(descripcion= "Puerto de Barranqueras con Santiago del Estero", es_correcta= False, id_resp=3)
	x = [r16, r17, r18]

	p6 = Preg(descripcion="El ex ferrocarril general Belgrano conectaba a:", lista_respuestas= x)

	r19 = Resp(descripcion="Juan Manuel Silva", es_correcta= True, id_resp=1)
	r20 = Resp(descripcion="Giorgio Carrara", es_correcta= False, id_resp=2)
	r21 = Resp(descripcion= "Marcos Siebet", es_correcta= False, id_resp=3)
	x = [r19, r20, r21]

	p7 = Preg(descripcion="En el ambito automovilistico Chaco tiene un exponente a nivel nacional e internacional,¿Quien es?", lista_respuestas= x)

	r22 = Resp(descripcion="Basquet", es_correcta= True, id_resp=1)
	r23 = Resp(descripcion="Futbol", es_correcta= False, id_resp=2)
	r24 = Resp(descripcion= "Jockey", es_correcta= False, id_resp=3)
	x = [r22, r23, r24]

	p8 = Preg(descripcion="En el ambito de los juego olimpicos, Chaco tiene un medallista en:", lista_respuestas= x)

	r25 = Resp(descripcion="Natacion", es_correcta= False, id_resp=1)
	r26 = Resp(descripcion="Remo", es_correcta= False, id_resp=2)
	r27 = Resp(descripcion= "Atletismo", es_correcta= True, id_resp=3)
	x = [r25, r26, r27]

	p9 = Preg(descripcion="Marcela Gomez, chaqueña, participo en los juegos Olimpicos de tokio en:", lista_respuestas= x)

	r28 = Resp(descripcion="For Ever", es_correcta= False, id_resp=1)
	r29 = Resp(descripcion="Sarmiento", es_correcta= True, id_resp=2)
	r30 = Resp(descripcion= "Don Orione", es_correcta= False, id_resp=3)
	x = [r28, r29, r30]

	p10 = Preg(descripcion="El club de futbol mas antiguo del Chaco es", lista_respuestas= x)

	r31 = Resp(descripcion="Acordeon", es_correcta= False, id_resp=1)
	r32 = Resp(descripcion="N´vike", es_correcta= True, id_resp=2)
	r33 = Resp(descripcion= "Charango", es_correcta= False, id_resp=3)
	x = [r31, r32, r33]

	p11 = Preg(descripcion='Por Decreto N° 1491 el Gobierno de la Provincia del Chaco se declaro a un instrumento musical como' "Patrimonio Cultural de la provincia del Chaco, ¿Cual es?", lista_respuestas= x)

	ctx["form"] = PreguntasForm2(preguntas=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11])

	return render(request,template_name,ctx)

