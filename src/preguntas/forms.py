from django import forms


class PreguntasForm(forms.Form):
	pregunta = forms.CharField(label="Responda la siguiente pregunta: ",widget=forms.TextInput(attrs={'class':'form-control'}))

	respuestas = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

	def __init__(self, pregunta, respuestas, *args, **kwargs):
	    super(PreguntasForm, self).__init__(*args, **kwargs)
	    self.fields["pregunta"].initial = pregunta
	    self.fields["pregunta"].widget.attrs["readonly"] = True

	    self.fields["respuestas"].choices = respuestas

class PreguntasForm2(forms.Form):
	def __init__(self, preguntas, *args, **kwargs):
	    super(PreguntasForm2, self).__init__(*args, **kwargs)
	    for i, p in enumerate(preguntas):
	    	nro_pregunta = i+1
	    	self.fields[f"pregunta_{nro_pregunta}"] = forms.CharField(label=f"Pregunta {nro_pregunta}", initial=p.descripcion)
	    	self.fields[f"pregunta_{nro_pregunta}"].widget.attrs["class"] = 'form-control'
	    	self.fields[f"pregunta_{nro_pregunta}"].widget.attrs["readonly"] = True

	    	self.fields[f"pregunta_opciones_{nro_pregunta}"] = forms.MultipleChoiceField(label="Seleccione una opcion", choices=[(r.id_resp, r.descripcion) for r in p.lista_respuestas], widget=forms.RadioSelect)
"""
class PreguntaForm(forms.ModelForm): 
	class Meta:
		model = pregunta
		fields = ["nombre", "apellido"]
"""