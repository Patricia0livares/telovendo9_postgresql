from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from .models import Mensaje, Proveedor
from .models import NombreFantasia

# from bootstrap_blog.blogapp.models import Mensaje


class RegistroClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50, required=True)
    apellido=forms.CharField(max_length=50, required=True)
    apellidoM=forms.CharField(max_length=50, required=True)
    correo=forms.CharField(widget=forms.EmailInput)
    pais=forms.CharField(max_length=50, required=True)

class RegistroProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields=('nombre_fantasia','razon_social','contacto','correo','servicio','categoria')
#    #donde se pone que sea email con @
#     correo=forms.EmailField(widget=forms.EmailInput)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class MensajeForm(forms.ModelForm):
    
	class Meta:
		model = Mensaje
		fields=('nombre','correo','mensaje','tipo_mensaje')