from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import User

user = get_user_model()

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
                raise forms.ValidationError("Este Usuario No Existe")
            if not user.check_password(password):
                raise forms.ValidationError("Contraseña Incorrecta")
            if not user.is_active:
                raise forms.ValidationError("Este Usuario No está Activo")
        return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)

class RegistroFormulario(UserCreationForm):
    nombre =forms.CharField(required = True)
    apellido = forms.CharField(required = True)
    class Meta :
        model = user
        fields = [

        'nombre',
        'apellido',
        'username',
        'password1'

        ]
			
#################################################################