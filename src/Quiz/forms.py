from django import forms

from .models import  Pregunta, ElegirRespuesta, PreguntasRespondidas

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class ElegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == Pregunta.NUMER_DE_RESPUESTAS_PERMITIDAS
		except AssertionError:
			raise forms.ValidationError("Ingresar una unica respuesta correcta")

#################################################################
class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Este usuario No existe")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("Este Usuario No esta activo")

		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)



class RegistroFormulario(UserCreationForm):
	nombre = forms.CharField(required=True)
	apellido = forms.CharField(required=True)

	class Meta:
		model = User 

		fields = [

		 'nombre',
        'apellido',
        'username',
        'password1'
		]
