from django.db import models


# Create your models here.
# Relación uno a uno. Proveedor, Razón Social y Nombre de Fantasía
# Relación uno a muchos. Tipo de Mensaje, Un tipo de mensaje y muchos Mensajes
# Relación muchos a muchos. Proveedor y TipoServicio, Un tipo de servicio muchos proveedores, Un proveedor muchos tipos de servicio

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    apellidoM=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    pais=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class NombreFantasia(models.Model):
    nombre_fantasia=models.CharField(max_length=50)
       
    def __str__(self):
        return self.nombre_fantasia

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    servicio = models.ManyToManyField(Servicio)
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    #Key onetoone
    nombre_fantasia=models.OneToOneField(NombreFantasia, blank= True, null=True, on_delete=models.SET_NULL)
    razon_social=models.CharField(max_length=50)
    contacto=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    servicio=models.ManyToManyField(Servicio)
    categoria=models.ManyToManyField(Categoria)
      
    def __str__(self):
        return '%s %s' % (self.nombre_fantasia, self.razon_social)

class TipoMensaje(models.Model):
    tipo_mensaje=models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_mensaje

class Mensaje(models.Model):
    nombre=models.CharField(max_length=50, verbose_name= 'nombre')
    correo=models.EmailField(max_length=100, verbose_name= 'correo')
    mensaje=models.CharField(max_length=200, verbose_name= 'mensaje')
    #Key Tipo de Mensaje
    tipo_mensaje=models.ForeignKey(TipoMensaje, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre

