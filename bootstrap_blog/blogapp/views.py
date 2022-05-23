from blogapp.models import Cliente

from django.shortcuts import redirect, render
from .models import Cliente, Proveedor, Mensaje
from .forms import RegistroClienteForm, RegistroProveedorForm, MensajeForm
# from .forms import LoginForm, UserRegisterForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import NewUserForm
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def index(request):
    return render(request,"blogapp/index.html")

def usuarios(request):
    usuario=Cliente.objects.all()
    return render (request, 'blogapp/usuarios.html', {"data":usuario})

def ingreso(request):
    form = RegistroClienteForm()

    if request.method == 'POST':
        
        form = RegistroClienteForm(request.POST)

        if form.is_valid():

            cliente=Cliente()
            cliente.nombre=form.cleaned_data["nombre"]
            cliente.apellido=form.cleaned_data["apellido"]
            cliente.apellidoM=form.cleaned_data["apellidoM"]
            cliente.correo=form.cleaned_data["correo"]
            cliente.pais=form.cleaned_data["pais"]
            cliente.save()
            return redirect('ingreso')

        else:
            print('invalido')

    return render(request, 'blogapp/ingreso.html',{'form':form})

@staff_member_required
@login_required
def ingresoproveedor(request):
    form = RegistroProveedorForm()

    if request.method == 'POST':
        form = RegistroProveedorForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Proveedor creado exitosamente.')
            return redirect('proveedor')

        else:
            print('invalido')

    return render(request, 'blogapp/proveedor.html',{'form':form})

def login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        
        if form.is_valid():
            usuario=form.cleaned_data["username"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
                return redirect ('index')
            else:
                messages.error(request,"Nombre o contraseña no válidos.")
                form=LoginForm()
                return render (request, 'blogapp/login.html', {"login_form":form})   
        else:
            messages.error(request,"Nombre o contraseña no válidos.")
            form=LoginForm()
            return render (request, 'blogapp/login.html', {"login_form":form})
    else:
        form=LoginForm()
        return render (request, 'blogapp/login.html', {"login_form":form})

def register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:

        form = NewUserForm()
    context = {'form':form}
    return render(request, 'blogapp/register.html', context)

@login_required
def logout_user(request):
	logout(request)
	messages.info(request, "Haz cerrado sesión exitosamente.") 
	return redirect('index')

def mensaje_cliente(request):
    mensajes=Mensaje.objects.all()
    return render (request, 'blogapp/mensajes.html', {"data":mensajes})

@staff_member_required
@login_required
def ingreso_mensaje(request):
    form = MensajeForm()

    if request.method == 'POST':
        
        form = MensajeForm(request.POST)

        #INCLUIR INSTANCIA?

        if form.is_valid():

            mensaje_nuevo=Mensaje()
            mensaje_nuevo.nombre=form.cleaned_data["nombre"]
            mensaje_nuevo.correo=form.cleaned_data["correo"]
            mensaje_nuevo.mensaje=form.cleaned_data["mensaje"]
            mensaje_nuevo.tipo_mensaje=form.cleaned_data["tipo_mensaje"]
            mensaje_nuevo.save()
            messages.success(request, f'Gracias por contactarnos')
            return redirect('mensajes')

        else:
            print('invalido')

    return render(request, 'blogapp/ingreso_mensaje.html',{'formp':form})

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

@login_required
def mensaje_edit(request,pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    if request.method == "POST":
        form = MensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.save()
            messages.success(request, 'Hemos recibido su mensaje, gracias')
            return redirect('mensajes')
    else:
        form = MensajeForm(instance=mensaje)
    return render(request, 'blogapp/mensaje_edit.html', {'form': form})

@login_required
def mensaje_delete(request,pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    mensaje.delete()
    messages.success(request, 'Mensaje eliminado, gracias')        
    return redirect('mensajes')