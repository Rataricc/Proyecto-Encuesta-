from django.contrib import admin

from .models import Pregunta, Opcion

class OpcionInline(admin.TabularInline):
	model = Opcion
	extra = 3
class PreguntaAdmin(admin.ModelAdmin):
	fieldsets = [
			(None,									 {'fields':['pregunta_text']}),
			('Date_information', {'fields':['fecha_publ'],'classes':['collapse']}),
			]
	inlines = [OpcionInline]

	list_display = ['pregunta_text','fecha_publ']
			
		

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Opcion)