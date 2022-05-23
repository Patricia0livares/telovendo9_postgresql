from django.contrib import admin
from .models import Cliente, Proveedor,Mensaje,TipoMensaje,NombreFantasia,Servicio,Categoria
from . import models

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(NombreFantasia)
admin.site.register(Mensaje)
admin.site.register(TipoMensaje)
admin.site.register(Servicio)
admin.site.register(Categoria)
